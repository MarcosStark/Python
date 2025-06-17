from class_employers import Employers
from functions import full_name, age

employer1 = Employers("Marcos", "Menezes", 1998, 2500)
employer2 = Employers("Alan", "Marcelino", 1997, 3000)

# Printando as innformações de nome completo dos usuários.
print(full_name(employer1))
print(full_name(employer2))

print(age(employer1))
print(age(employer2))
