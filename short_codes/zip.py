#A função zip concatena duas listas

list1 = ["First_Name", "Second_Name", "Third_Name", "Fourth_Name", "Last_Name"]
list2 = ["Marcos", "Augusto", "Rodrigues", "De", "Menezes"]

#Pega o 1º elemento da ista 1 e concatena com o 1º elemento a lista 2 e assim por diante
for position, name in  zip(list1, list2):
    print(position, name)
