#Números ao quadrado
"""list1 = [2, 3, 4, 5, 6, 7]
list2 = [num**2 for num in list1] #Pegará cada número e elevará ao quadrado

print(list2)

#Retorna uma lista apenas com os números ímpares da lista 1
list3 = [num for num in list1 if num%2==1]
print(list3)"""

#De forma extensa
fruits1 = ["manga", "acerola", "banana", "sapoti"]
fruits2 = []

for item in fruits1:
    if "s" in item:
        fruits2.append(item)
print(fruits2)

#De forma resumida
print([item for item in fruits1 if "s" in item])

values1 = []
from sys import getsizeof
print("Size:", getsizeof([x * 10 for x in range(11)])) #Dada a expressao, para cada item no range 11, esta sera aplicada.

#Generator Expressions: Ocupa muito menos espaço na memoria quando a lista e grande e sofrera alteracoes
print("Size:", getsizeof((x * 10 for x in range(11))))
print(list((x * 10 for x in range(11))))