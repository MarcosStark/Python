import random

#Método randint: Gera um número aletório.

number = random.randint(0, 100)

#Recebe o palpite do usuário
guess = int(input("Advinhe o número entre 0 e 100 que o computador pensou: "))

#Verifca se o usuário acertou
if(guess == number):
    print("Você acertou !!!")
else:
    print("Você errou !!!")