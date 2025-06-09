alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def encript():
    msg_encripted = ""
    print("Mensagem a encriptar:")
    msg = input("Mensagem: ")

    for i in msg:
        msg_encripted = str(msg_encripted) + alphabet[alphabet.index(i) + 3]
    print(msg_encripted, end="\n")

    print("Deseja encriptar outra mensagem?")
    option = input("R: ")
    if option == "sim":
        encript()
    else:
        print("Deseja desencriptar uma mensagem?")
        option2 = input("R: ")
        if option2 == "sim":
            uncript()
        else:
            pass


def uncript():
    msg_encripted = ""
    print("Mensagem a desincriptar:")
    msg = input("Mensagem: ")

    for i in msg:
        msg_encripted = str(msg_encripted) + alphabet[alphabet.index(i) - 3]
    print(msg_encripted, end="\n")

print("Deseja encriptar ou desencriptar uma mensagem? ")
r = input("R: ")

if r == "encriptar":
    encript()
elif r == "desencriptar":
    uncript()
else:
    print("Opção inválida")