import datetime # Importa o módulo 'datetime' para trabalhar com datas e horas.

# Obtém a hora atual do sistema (um número inteiro entre 0 e 23).
current_time = datetime.datetime.now().hour

# Verifica se a hora atual é menor que 12 (antes do meio-dia).
if current_time < 12:
    print("Good morning!")
# Caso contrário, verifica se a hora atual é menor que 18 (antes das 18h).
elif current_time < 18:
    print("Good afternoon!")
# Se nenhuma das condições anteriores for verdadeira (ou seja, a hora é 18h ou mais).
else:
    print("Good evening!")
