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

articles = []

#Nome do rquivo CSV

file_name = "articles.csv"
with open(file_name, "a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    #Cabeçalho do artigo
    writer.writerow(["Title", "Author", "Year", "Journal"])

    """#Escrever os dados de cada objeto.
    for article in articles:
        writer.writerow(article.to_csv_row())"""

def articles_informations():
    title = input("Informe o título do artigo: ")
    author = input("Informe o autor do artigo: ")
    year = input("Informe o ano do artigo: ")
    journal = input("Informe o journal do artigo: ")
    writer.writerow([title, author, year, journal])



print("Exportados com sucesso!")