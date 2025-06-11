import secrets
import string

def password_generator(length = 15):
    alphanumeric_characters = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphanumeric_characters) for i in range(length))
    return key

key  = password_generator()
print({key})

