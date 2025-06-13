#A função zip concatena duas listas

list1 = [1, 2, 3, 4, 5]
list2 = ["First_Name", "Second_Name", "Third_Name", "Fourth_Name", "Last_Name"]
list3 = ["Marcos", "Augusto", "Rodrigues", "De", "Menezes"]

#Pega o 1º elemento da ista 1 e concatena com o 1º elemento a lista 2 e assim por diante
for index, position, name in  zip(list1, list2, list3):
    print(index, position, name, )
