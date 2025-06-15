#Código para classificar artigos e salvar trechos importantes.
import csv

class Article:
    def __init__(self,title,author,year,journal):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal

#Metodo para retornar os dados do objeto em um formato de lista para o CSV
    def to_csv_row(self):
        return [self.title, self.author, self.year, self.journal]

#Nome do rquivo CSV
file_name = "articles.csv"

def articles_informations():
    title = input("Informe o título do artigo: ")
    author = input("Informe o autor do artigo: ")
    year = input("Informe o ano do artigo: ")
    journal = input("Informe o journal do artigo: ")

    with open(file_name, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Author", "Year", "Journal"])#Cabeçalho do artigo
        writer.writerow([title, author, year, journal])

    print("Informações salvas com sucesso!\n")

    awnser2 = input("Deseja salvar outro artigo? ").lower()
    articles_informations() if awnser2 == "sim" or awnser2 == "s" else None





#Entrada do usuário
print("Bem vindo(a) ao classificador de artigos")
awnser1 = input("Deseja salvar informações de um artigo? ").lower()
articles_informations() if awnser1 == "sim" or awnser1 == "s" else None

