import secrets # Usado para gerar números aleatórios criptograficamente seguros.
import string   # Fornece constantes de string como letras e dígitos.

def password_generator(length = 15):
    # Define o conjunto de caracteres alfanuméricos (letras maiúsculas, minúsculas e dígitos).
    alphanumeric_characters = string.ascii_letters + string.digits
    # Gera a senha escolhendo caracteres aleatoriamente do conjunto.
    key = ''.join(secrets.choice(alphanumeric_characters) for i in range(length))
    return key

# Gera uma senha com o comprimento padrão (15 caracteres).
key  = password_generator()
# Imprime a senha gerada.
print({key})
