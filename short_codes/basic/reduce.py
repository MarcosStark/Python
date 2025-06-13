#Importando a fucção reduce
from functools import reduce

#Definindo a função
def sum(x, y):
    return x + y

#Criando alista de teste
list1 = [1, 5, 10, 15, 20]

#Nesse caso o reduce pega o valor de y(na primeira rodada é 0) e soma com os valores iterados da lista, resentados por x
sum = reduce(sum, list1)
print(sum)