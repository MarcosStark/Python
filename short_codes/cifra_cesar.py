alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def encrypt():
    msg_encrypted = ""
    print("Mensagem a encriptar:")
    msg = input("Mensagem: ")

    for i in msg:
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) + 3]
    print(msg_encrypted, end="\n")

    print("Deseja encriptar outra mensagem?")
    option = input("R: ")
    if option == "sim":
        encrypt()
    else:
        print("Deseja desencriptar uma mensagem?")
        option2 = input("R: ")
        if option2 == "sim":
            decrypt()
        else:
            pass


def decrypt():
    msg_encrypted = ""
    print("Mensagem a desincriptar:")
    msg = input("Mensagem: ")

    for i in msg:
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) - 3]
    print(msg_encrypted, end="\n")

print("Deseja encriptar ou desencriptar uma mensagem? ")
r = input("R: ")

if r == "encriptar":
    encrypt()
elif r == "desencriptar":
    decrypt()
else:
    print("Opção inválida")