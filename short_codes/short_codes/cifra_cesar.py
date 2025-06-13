# Define o alfabeto para uso na encriptação e desencriptação.
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Função para criptografar uma mensagem.
def encrypt():
    msg_encrypted = ""
    print("Mensagem a criptografar:")
    msg = input("Mensagem: ")

    # Percorre cada caractere da mensagem e o encripta.
    for i in msg:
        # Adiciona 3 ao índice do caractere no alfabeto (cifra de César).
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) + 3]
    print(msg_encrypted, end="\n")

    # Oferece a opção de criptografar outra mensagem ou ir para a descriptografia.
    print("Deseja criptografar outra mensagem?")
    option = input("R: ")
    if option == "sim":
        encrypt()
    else:
        print("Deseja descriptografar uma mensagem?")
        option2 = input("R: ")
        if option2 == "sim":
            decrypt()
        else:
            pass

# Função para descriptografar uma mensagem.
def decrypt():
    msg_encrypted = ""
    print("Mensagem a descriptografar:")
    msg = input("Mensagem: ")

    # Percorre cada caractere da mensagem e o desencripta.
    for i in msg:
        # Subtrai 3 do índice do caractere no alfabeto para reverter a cifra.
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) - 3]
    print(msg_encrypted, end="\n")

    # Oferece a opção de descriptografar outra mensagem ou ir para a criptografia.
    print("Deseja descriptografar outra mensagem?")
    option = input("R: ")
    if option == "sim":
        encrypt()
    else:
        print("Deseja criptografar uma mensagem?")
        option2 = input("R: ")
        if option2 == "sim":
            encrypt()
        else:
            pass

# Ponto de entrada do programa: pergunta ao usuário o que deseja fazer.
print("Deseja criptografar ou descriptografar uma mensagem? ")
r = input("R: ")

# Chama a função apropriada com base na escolha do usuário.
if r == "criptografar":
    encrypt()
elif r == "descriptografar":
    decrypt()
else:
    print("Opção inválida")