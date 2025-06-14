#def: Palavra reservada para criar função
def double(x):
    return x * 2

list1 = [1, 2, 3, 4, 5]

#map: Aplica uma determinada função a cada item de um iterável
double_value = map(double, list1)

#Retorno sem formato de lista
for i in double_value:
    print(i)

#Ou retorno direto como lista
"""double_value = list(double_value)
print(double_value)"""

print(list(map(lambda x: x * 2, list1))) #Tudo resumido em uma linha utilizando lambda.

#list: Converte o resultado em lista.
#map: Executada a funcao lambda item por item.
#list1: Lista que sera percorrida.