import os
import requests # Para fazer chamadas HTTP diretas ao Ollama
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from opensearchpy import OpenSearch, NotFoundError
import json
from typing import List

# Carrega variáveis de ambiente do .env (ou do ambiente do Docker)
load_dotenv()

# Configurações do ambiente e dos modelos
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST")
OPENSEARCH_PORT = os.getenv("OPENSEARCH_PORT")
OPENSEARCH_URL = f"http://{OPENSEARCH_HOST}:{OPENSEARCH_PORT}"
INDEX_NAME = "meu_rag_index_puro" # Nome do índice no OpenSearch
EMBEDDING_MODEL = "mistral" # Modelo do Ollama para embeddings
LLM_MODEL = "mistral"      # Modelo do Ollama para geração de texto

# Inicializa o FastAPI
app = FastAPI(
    title="API RAG Pura (Sem LangChain)",
    description="Uma API de Geração Aumentada por Recuperação (RAG) implementada manualmente com Ollama e OpenSearch.",
    version="1.0.0",
)

# Cliente OpenSearch global, será inicializado no startup
opensearch_client = None

# Modelo Pydantic para validar a requisição de consulta
class QueryRequest(BaseModel):
    query: str

# --- Funções Auxiliares para Interagir com Ollama e OpenSearch ---

def get_ollama_embedding(text: str) -> List[float]:
    """
    Obtém embeddings (representações vetoriais) de um texto
    usando a API de embeddings do Ollama.
    """
    url = f"{OLLAMA_BASE_URL}/api/embeddings"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": EMBEDDING_MODEL,
        "prompt": text
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() # Lança exceção para status de erro (4xx ou 5xx)
        return response.json()["embedding"]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter embedding do Ollama: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao obter embedding do Ollama: {e}")

def get_ollama_completion(prompt: str) -> str:
    """
    Obtém uma resposta gerada pelo LLM do Ollama,
    dado um prompt.
    """
    url = f"{OLLAMA_BASE_URL}/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False # Não queremos streaming para esta demonstração
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        # A API do Ollama retorna a resposta final dentro do campo 'response'
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter resposta do Ollama: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao obter resposta do Ollama: {e}")

def simple_text_splitter(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """
    Divide um texto longo em pedaços (chunks) menores.
    Esta é uma implementação simples e pode ser melhorada para produção.
    """
    chunks = []
    current_pos = 0
    while current_pos < len(text):
        end_pos = min(current_pos + chunk_size, len(text))
        chunk = text[current_pos:end_pos]
        chunks.append(chunk)
        current_pos += (chunk_size - overlap)
        if current_pos >= len(text) - overlap and end_pos == len(text):
            break # Evita loops infinitos ou pedaços muito pequenos no final
    return chunks

# --- Evento de Inicialização da API (Startup) ---

@app.on_event("startup")
async def startup_event():
    """
    Esta função é executada uma vez quando a API inicia.
    Ela se conecta ao OpenSearch e ingere os documentos, se o índice não existir.
    """
    print(f"Iniciando API (sem LangChain) e conectando ao OpenSearch em: {OPENSEARCH_URL}")
    global opensearch_client

    try:
        # Conecta ao cliente OpenSearch
        opensearch_client = OpenSearch(
            hosts=[{'host': OPENSEARCH_HOST, 'port': OPENSEARCH_PORT}],
            http_compress=True,
            http_auth=('admin', 'admin'), # Credenciais padrão para setup local sem segurança
            use_ssl=False, # Não usar SSL para setup local simples
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

        # Verifica se o cluster OpenSearch está saudável
        try:
            health = opensearch_client.cluster.health()
            print(f"Status do cluster OpenSearch: {health['status']}")
            if health['status'] not in ['green', 'yellow']:
                raise ConnectionError("Cluster OpenSearch não está saudável. Status: " + health['status'])
        except Exception as e:
            print(f"Erro ao verificar o status do cluster OpenSearch: {e}")
            raise HTTPException(status_code=500, detail=f"Erro ao conectar ou cluster OpenSearch não está saudável: {e}")

        # Verifica se o índice já existe no OpenSearch
        if opensearch_client.indices.exists(index=INDEX_NAME):
            print(f"Índice '{INDEX_NAME}' já existe. Pronto para buscas.")
        else:
            print(f"Índice '{INDEX_NAME}' não encontrado. Criando e iniciando ingestão de dados...")

            # Define o mapeamento do índice para armazenamento de vetores (embeddings)
            index_body = {
                'settings': {
                    'index.knn': True, # Habilita o plugin k-NN para busca vetorial
                    'number_of_shards': 1,
                    'number_of_replicas': 0
                },
                'mappings': {
                    'properties': {
                        'text_content': {'type': 'text'}, # O texto original
                        'embedding': {
                            'type': 'knn_vector',
                            'dimension': 4096 # Dimensão do embedding do Mistral 7B (Mistral Lite ou base)
                        }
                    }
                }
            }
            opensearch_client.indices.create(index=INDEX_NAME, body=index_body)
            print(f"Índice '{INDEX_NAME}' criado com sucesso.")

            # Carrega o texto do arquivo e divide em pedaços
            with open("./data/documents.txt", "r", encoding="utf-8") as f:
                full_text = f.read()

            documents_chunks = simple_text_splitter(full_text, chunk_size=200, overlap=50) # Ajuste esses valores!

            print(f"Documentos divididos em {len(documents_chunks)} partes. Gerando embeddings e inserindo no OpenSearch...")

            # Para cada pedaço, gera o embedding e insere no OpenSearch
            for i, chunk in enumerate(documents_chunks):
                embedding = get_ollama_embedding(chunk)
                doc = {
                    "text_content": chunk,
                    "embedding": embedding
                }
                # Insere o documento no índice, usando o índice do loop como ID
                opensearch_client.index(index=INDEX_NAME, body=doc, id=i)
            opensearch_client.indices.refresh(index=INDEX_NAME) # Garante que os documentos estejam pesquisáveis imediatamente
            print("Ingestão de dados concluída no OpenSearch.")

    except Exception as e:
        print(f"ERRO CRÍTICO DURANTE A INICIALIZAÇÃO: {e}")
        # Levanta uma exceção HTTP para que o FastAPI saiba que houve um erro grave
        raise HTTPException(status_code=500, detail=f"Erro na inicialização da API ou ingestão de dados: {e}. Verifique os logs do Docker para mais detalhes.")

# --- Endpoints da API ---

@app.get("/")
async def read_root():
    return {"message": "API RAG Pura (Sem LangChain) está rodando! Acesse /docs para testar."}

@app.post("/query")
async def rag_query(request: QueryRequest):
    """
    Endpoint principal para processar uma pergunta do usuário usando RAG.
    """
    if not opensearch_client or not opensearch_client.indices.exists(index=INDEX_NAME):
        raise HTTPException(status_code=503, detail="Serviço indisponível: OpenSearch não está pronto ou índice não foi criado.")

    try:
        # 1. Obter o embedding da pergunta do usuário
        query_embedding = get_ollama_embedding(request.query)

        # 2. Buscar os documentos mais relevantes no OpenSearch (busca k-NN por similaridade)
        search_body = {
            "size": 3, # Recuperar os 3 documentos mais similares
            "query": {
                "knn": {
                    "embedding": {
                        "vector": query_embedding,
                        "k": 3 # k-nearest neighbors
                    }
                }
            },
            "_source": ["text_content"] # Queremos apenas o conteúdo do texto dos documentos encontrados
        }
        response = opensearch_client.search(index=INDEX_NAME, body=search_body)

        # Extrai o conteúdo dos documentos encontrados
        context_documents = [hit['_source']['text_content'] for hit in response['hits']['hits']]
        context = "\n\n".join(context_documents) # Junta os documentos em um único string de contexto

        if not context:
            return {"response": "Não consegui encontrar informações relevantes nos documentos para sua pergunta."}

        # 3. Construir o prompt completo para o LLM, incluindo o contexto
        prompt = f"""Use o seguinte contexto para responder à pergunta.
        Se a resposta não estiver no contexto, diga que não sabe.

        Contexto:
        {context}

        Pergunta: {request.query}
        Resposta:
        """

        # 4. Chamar o LLM (Mistral 7B via Ollama) para gerar a resposta
        llm_response = get_ollama_completion(prompt)

        return {"response": llm_response}

    except Exception as e:
        print(f"Erro ao processar a consulta RAG: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar a consulta: {e}. Detalhes: {str(e)}")