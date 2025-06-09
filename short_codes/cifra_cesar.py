alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
key = ""
input_value = ""

while input_value != "enviar":
    input_value = input("Digite a letra: ")

    if input_value != "enviar":
        key = str(key) + alphabet[alphabet.index(input_value) - 3]
    else:
        for i in key:
            print(i, end="")


    

