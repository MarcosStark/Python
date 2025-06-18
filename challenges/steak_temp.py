temp = int(input("Informe a temperatura(ºc) da carne: "))

if temp < 48:
    print("Cozinhe por mais alguns minutos para SELAR a carne.")
elif temp == 48:
    print("A carne esta SELADA.")
elif temp in range(49, 53):
    print("Cozinhe por mais alguns minutos para alcançar AO PONTO PARA MAL.")
elif temp == 54:
    print("A carne esta AO PONTO PARA MAL.")
elif temp in range(55, 59):
    print("Cozinhe por mais alguns minutos para alcançar AO PONTO.")
elif temp == 60:
    print("A carne esta AO PONTO.")
elif temp in range(61, 64):
    print("Cozinhe por mais alguns minutos para alcançar AO PONTO PARA BEM.")
elif temp == 65:
    print("A carne esta AO PONTO PARA BEM.")
elif temp in range(66, 70):
    print("Cozinhe por mais alguns minutos para alcançar BEM PASSADA.")
elif temp == 71:
    print("A carne esta BEM PASSADA.")
else:
    print("A carne esta QUEIMADA.")