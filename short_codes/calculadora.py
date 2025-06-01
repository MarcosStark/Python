#Define as variáveis necessárias
number1 = float(input("Informe o 1º número: "))
signal = input("Informme a operação: ")
number2 = float(input("Informe o 2º número: "))

#Realiza o cálculo de acordo com a operação escolhida pelo usuário
if signal == "+":
    result = number1 + number2
    print(result)
elif signal == "-":
    result = number1 - number2
    print(result)
elif signal == "*":
    result = number1 * number2
    print(result)
elif signal == "/":
    result = number1 / number2
    print(result)
else:
    print("Inválido!")
