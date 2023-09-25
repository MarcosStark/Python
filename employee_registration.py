# -*- coding: utf-8 -*-
#exercise 01 @Marcos Augusto

employee = {"name": "", "cpf": "", "role": "", "payment": int, "workload": ""}
event = {"name": "", "type": ""}
release = {"employee": "", "event": "", "value": int}

op = ""

while op != "sim":
    employee["name"] = input("Nome do funcionário: ")
    employee["cpf"] = input("CPF: ")
    employee["role"] = input("Função: ")
    employee["payment"] = float(input("Remuneração: "))
    employee["workload"] = input("Carga horária: ")

    print(employee)

    eventop = input("Adicionar um evento? ")

    if eventop == "sim":
      event["name"] = input("Nome do evento: ")
      event["type"] = input("Tipo do evento: ")

    lancop = input("Adicionar um lançamento? ")

    if lancop == "sim":
      release["employee"] = input("Funcionário: ")
      release["event"] = input("Evento: ")
      release["value"] = float(input("Valor R$ "))

      if release["employee"] == employee["name"] and event["type"] == "desconto" and event["name"] == "falta":
        employee["payment"] = employee["payment"] - release["value"]

      elif release["employee"] == employee["name"] and event["type"] == "vencimento" and event["name"] == "bonus":
        employee["payment"] = employee["payment"] + release["value"]
      
      else:
        print("Lançamento inválido!")

    else:
      print(employee)
      op  = input("Deseja encerrar? ")