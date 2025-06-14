def inventory_items(name, qtd, value): #Define os parametros.
    print(f"Item: {name}\nQuantity: {qtd}\nValue: {value}")

inventory_items("Notebook", 3, 3000) #Informa os argumentos.

#print: Printa na tela sem armazenar.
#return: Armazena o valor, que pode ser printado depois.

def inventory(*item): #Deifine que posso informar inumeros argumentos.
    return item
print(inventory("Notebook", 3, 3000, "Asus")) #Informo inumeros parametros com inumeros argumentos.

def inventory(**item): #Deifine que posso informar inumeros parametros
    return item
print(inventory(name = "Notebook", quantity = 3, value = 3000, marca = "Asus")) #Informo inumeros parametros com inumeros argumentos.
