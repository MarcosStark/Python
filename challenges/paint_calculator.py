#Calculadora de pintura
import math
def area_calc():
    if data[1] == data[2]:
        calc = (4 * int(data[1]))
        print(calc)
        return calc
    else:
        calc = int(data[1]) * int(data[2])
        print(calc)
        return calc

def paint_calc(calc):
    performance = calc / int(data[0])
    performance = math.ceil(performance)
    print(f"Você necessitará de {performance} latas de tinta.")


data = input("Informe o rendimento da lata de tinta e altura e largura da parede, com vírgulas: ").split(",")
area_calc = area_calc()
paint_calc(area_calc)
