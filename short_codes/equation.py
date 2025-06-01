import math

#Definindo a equação
a = 1 
b = 3
c = 0

#Encontrando o delta da equação
delta = (((b**2)-(4*a)*c))
print("Delta: " + str(delta))

#Encontrando x' e x''
x1 = ((-b + math.sqrt(delta)) / 2*a)
print("x': " + str(x1))

x2 = ((-b - math.sqrt(delta)) / 2*a)
print("x'': " + str(x2))



