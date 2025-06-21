list1 = [10, 30, 50, 100]
list2 = [20, 30, 40, 50, 90]

result1 = set(list1)
result2 = set(list2)

print(result1 | result2) #Union: Retorna a junçao das listas, sem repetir numeros.
print(result1 & result2) #Intersection: Retorna o que existe nas duas listas.
print(result1 ^ result2) #Symetric Difference: Retorna os valores, excetuando os que existem nas duas listas.
print(result1 - result2) #Difference: Retorna o que existe na primeira lista e nao existe na segunda lista.

print("Methods")
print(result1.union(result2))
print(result1.intersection(result2))
print(result1.symmetric_difference(result2))
print(result1.difference(result2))

#Consultar documentacao para mais.

