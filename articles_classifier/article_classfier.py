#Código para classificar artigos e salvar trechos importantes.
import csv

class Article:
    def __init__(self,title,author,year,journal,objective,methodology,results,conclusions,*key_excerpts,observations):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal
        self.objective = objective
        self.methodology = methodology
        self.results = results
        self.conclusions = conclusions
        self.key_excerpts = key_excerpts
        self.observations = observations

#Nome do rquivo CSV
file_name = "articles.csv"

def articles_informations():
    title = input("Informe o título do artigo: ")
    author = input("Informe o autor do artigo: ")
    year = input("Informe o ano do artigo: ")
    journal = input("Informe o journal do artigo: ")
    objective = input("Informe o objetivo do artigo: ")
    methodology = input("Informe a metodologia do artigo: ")
    results = input("Informe os resultados do artigo: ")
    conclusions = input("Informe os conclusões do artigo: ")
    key_excerpts = input("Informe os trechos mais importantes que você destacou, sempre citando a página(Ex: IA generativa. Pag 10):")
    observations = input("Informe as observações do artigo: ")

    with open(file_name, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Author", "Year", "Journal", "Objective", "Methodology", "Results", "Conclusions", "Key Excerpts", "Observations"])#Cabeçalho do artigo
        writer.writerow([title, author, year, journal, objective, methodology, results, conclusions, key_excerpts, observations])

    print("Informações salvas com sucesso!\n")

    awnser2 = input("Deseja salvar outro artigo? ").lower()
    articles_informations() if awnser2 == "sim" or awnser2 == "s" else print("Volte sempre que precisar!")





#Entrada do usuário
print("Bem vindo(a) ao classificador de artigos.")
awnser1 = input("Deseja salvar informações de um artigo? ").lower()
articles_informations() if awnser1 == "sim" or awnser1 == "s" else print("Volte sempre que precisar!")

