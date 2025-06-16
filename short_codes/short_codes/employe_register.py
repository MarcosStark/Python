from _datetime import datetime

#Cria a classe e o construtor, com seus atributos.
class Employers:
    def __init__(self, name, last_name, born_year, salary):
        self.name = name
        self.last_name = last_name
        self.born_year = born_year
        self.salary = salary

    #Method que retorna o nome completo.
    def full_name(self):
        return f"O nome do(a) colaborador(a) é {self.name} {self.last_name}."

    #Method que retorna a idade do usuário
    def age(self):
        actual_year = datetime.now().year
        age = actual_year - self.born_year
        return f"A idade do(a) colaborador(a) {self.full_name()} é: {age}."
    
employer1 = Employers("Marcos", "Menezes", 1998, 2500)
employer2 = Employers("Alan", "Marcelino",1997, 3000)

#print(employer1.full_name())
#print(employer2.full_name())

#Printando as innformações de nome completo dos usuários.
print(Employers.full_name(employer1))
print(Employers.full_name(employer2))

print(Employers.age(employer1))
print(Employers.age(employer2))