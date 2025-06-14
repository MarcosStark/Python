temp = float(input("Enter the temperature in Celsius: "))

if temp < 10:
    print("O clima está muito frio. Agasalhe-se.")
elif temp < 20 and temp > 10:
    print("O clima está fresco. Convém algum agasalho, se não gosta de frio.")
else:
    print("O clima está quente.")