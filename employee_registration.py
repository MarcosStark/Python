# -*- coding: utf-8 -*-
#exercise 01 @Marcos Augusto

funcionario = {"nome": "", "cpf": "", "funcao": "", "remuneracao": int, "carga_horaria": ""}
event = {"nome": "", "tipo": ""}
lancamento = {"funcionario": "", "evento": "", "valor": int}

op = ""

while op != "sim":
    funcionario["nome"] = input("Nome do funcionário: ")
    funcionario["cpf"] = input("CPF: ")
    funcionario["funcao"] = input("Função: ")
    funcionario["remuneracao"] = float(input("Remuneração: "))
    funcionario["carga_horaria"] = input("Carga horária: ")

    print(funcionario)

    eventop = input("Adicionar um evento? ")

    if eventop == "sim":
      event["nome"] = input("Nome do evento: ")
      event["tipo"] = input("Tipo do evento: ")

    lancop = input("Adicionar um lançamento? ")

    if lancop == "sim":
      lancamento["funcionario"] = input("Funcionário: ")
      lancamento["evento"] = input("Evento: ")
      lancamento["valor"] = float(input("Valor R$ "))

    if lancamento["funcionario"] == funcionario["nome"] and event["tipo"] == "desconto":
      if event["nome"] == "falta":
         funcionario["remuneracao"] = funcionario["remuneracao"] - lancamento["valor"]

    if lancamento["funcionario"] == funcionario["nome"] and event["tipo"] == "vencimento":
      if event["nome"] == "bonus":
         funcionario["remuneracao"] = funcionario["remuneracao"] + lancamento["valor"]

    print(funcionario)
    op  = input("Deseja encerrar? ")