#Cria a classe e o construtor, com seus atributos.
class Employers:
    def __init__(self, name, last_name, age, salary):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    #Method que retorna o nome completo.
    def full_name(self):
        return f"O nome do(a) colaborador(a) é {self.name} {self.last_name}."
    
employer1 = Employers("Marcos", "Menezes", 22, 2500)
employer2 = Employers("Alan", "Marcelino",25, 3000)

#print(employer1.full_name())
#print(employer2.full_name())

#Printando as innformações de nome completo dos usuários.
print(Employers.full_name(employer1))
print(Employers.full_name(employer2))