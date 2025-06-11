# Define a list representing the English alphabet in uppercase.
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Define the encryption function.
def encrypt():
    # Initialize an empty string to store the encrypted message.
    msg_encrypted = ""
    # Prompt the user to enter the message to be encrypted.
    print("Mensagem a encriptar:")
    msg = input("Mensagem: ")

    # Iterate through each character in the input message.
    for i in msg:
        # Find the index of the current character in the alphabet list.
        # Add 3 to the index to shift the character.
        # Append the shifted character to the encrypted message string.
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) + 3]
    # Print the encrypted message, followed by a new line.
    print(msg_encrypted, end="\n")

    # Ask the user if they want to encrypt another message.
    print("Deseja encriptar outra mensagem?")
    option = input("R: ")
    # If the user chooses "sim" (yes), call the encrypt function recursively.
    if option == "sim":
        encrypt()
    # Otherwise, ask the user if they want to decrypt a message.
    else:
        print("Deseja desencriptar uma mensagem?")
        option2 = input("R: ")
        # If the user chooses "sim" (yes), call the decrypt function.
        if option2 == "sim":
            decrypt()
        # Otherwise, do nothing (pass).
        else:
            pass

# Define the decryption function.
def decrypt():
    # Initialize an empty string to store the decrypted message.
    msg_encrypted = ""
    # Prompt the user to enter the message to be decrypted.
    print("Mensagem a desincriptar:")
    msg = input("Mensagem: ")

    # Iterate through each character in the input message.
    for i in msg:
        # Find the index of the current character in the alphabet list.
        # Subtract 3 from the index to shift the character back.
        # Append the shifted character to the decrypted message string.
        msg_encrypted = str(msg_encrypted) + alphabet[alphabet.index(i) - 3]
    # Print the decrypted message, followed by a new line.
    print(msg_encrypted, end="\n")

# Ask the user whether they want to encrypt or decrypt a message.
print("Deseja encriptar ou desencriptar uma mensagem? ")
r = input("R: ")

# If the user chooses "encriptar" (encrypt), call the encrypt function.
if r == "encriptar":
    encrypt()
# If the user chooses "desencriptar" (decrypt), call the decrypt function.
elif r == "desencriptar":
    decrypt()
# If the user enters an invalid option, print an error message.
else:
    print("Opção inválida")