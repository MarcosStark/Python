from datetime import datetime

# Method que retorna o nome completo.
def full_name(self):
    return f"O nome do(a) colaborador(a) é {self.name} {self.last_name}."


# Method que retorna a idade do usuário
def age(self):
    actual_year = datetime.now().year
    age1 = actual_year - self.born_year
    return f"A idade do(a) colaborador(a) {full_name(self)} é: {age1}."