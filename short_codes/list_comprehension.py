#Números ao quadrado
list1 = [2, 3, 4, 5, 6, 7]
list2 = [num**2 for num in list1] #Pegará cada número e elevará ao quadrado

print(list2)

#Retorna uma lista apenas com os números ímpares da lista 1
list3 = [num for num in list1 if num%2==1]
print(list3)