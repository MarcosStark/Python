alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
key = ""
input_option = ""

while input_option != "enviar":
    input_value = input("Digite a letra: ")
    input_option = input("Digite 'enviar' para finalizar ou 'continuar' para permanecer escrevendo: ")
    if (input_option !="enviar") and (input_option !="continuar"):
        print("Opção inválida.")
    else:
        key = str(key) + alphabet[alphabet.index(input_value) - 4]

for i in key:
    print(i)    
    

