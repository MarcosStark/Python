try:
    letters = ["a", "b", "c", "d", "e"]
    print(letters[5])
except IndexError:
    print("List index out of range.")

try:
    age = int(input("Informe sua idade: "))
    print(age)
except ValueError:
    print("Digite o valor em números.")
else:
    print("Sua idade foi registrada com sucesso.")
finally:
    print("Volte sempre!") #Será executado de qualquer forma.