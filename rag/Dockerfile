FROM python:3.9-slim-buster

WORKDIR /app 

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia ttodo o conteúdo da pasta atual para dentro do container
COPY . .

# Comando para iniciar sua aplicação FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]