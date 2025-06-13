msg = "Marcos Augusto"
name1 = "Marcos"
name2 = "Augusto"

print(msg[1]) #Retorna a letra que está na posição informada.
print(msg[0:6]) #Retorna todas as letras  da posição 0 a 5, 6 é a posição de parada.
print(msg[-7:-1]) #Retorna, de trás para frente, a qauntidade de letras informadas menos a primeira.
print(msg[-7:]) #Retorna, de trás para frente, a qauntidade de letras informadas.
print(msg.upper()) #Retorna o texto em letra maiúscula.
print(msg.lower()) #Retorna o texto em letra minúscula.
print(msg.strip()) #Elimina espaços desnecessários.
print(msg.replace("Augusto", "Menezes")) #Substitui o texto ou letra informado por outro também informado.
print(msg.split()) #Separa as palavras, retornando array.
print(f"Meu nome é {name1} {name2}.") #Utiliza a varável direto na frase, por meio do método f-string.

#Sequências de escape
msg2 = "O criador é \nMarcos Augusto." #Quebra a linha.
print(msg2)
msg2 = "O \tcriador \té \tMarcos \tAugusto." #Tabula a frase, cada palavra fica em uma coluna.
print(msg2)
msg2 = "c:\\Users\\Marcos" #Permite adicionar barra.
print(msg2)
msg2 = "O criador é \'Marcos Augusto\'." #Permite adicionar asppas.
print(msg2)

#Tabulando
msg3 = "Nome:\tMarcos Augusto\nIdade:\t26\nCidade:\tAracaju\nEstado:\tSergipe" #Retorna as informações em linhas e colunas.
print(msg3)

#Caracteres unicode. Existe uma tabela com oos códigos dos carcteres unicode.
msg4 = "Coração: \u2764" #Retorna o emoji de coração.
print(msg4)