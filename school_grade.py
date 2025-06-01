#Recebendo as notas do usuário
first_note = float(input("Informe sua 1ª nota: "))
second_note = float(input("Informe sua 2ª nota: "))


#Cálculo da nota
result = (first_note + second_note) / 2

#Condicional para verificar se o usuário éfoi aprovado ou não
if(str(result) >= "6"):
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")