#Dicionário
from xml.dom.minidom import ProcessingInstruction

meu_nome = {"A":"MARCOS", "B":"STARK"}

"""meu_nome.update({"A":"MARCOS"})
meu_nome.update({"C":"SIR"})

print(meu_nome.get("B"))
print(meu_nome)"""

#Para mais consultar documentacao

"""print(meu_nome["A"] + " " + meu_nome["B"])"""

#Usando laço de repetição

"""for key in meu_nome:
    print(key + "-" + meu_nome[key])"""

#Funções

#items(): Retorna todos os itens do dicionáro. Coneverte o dicionário em uma tupla(Conjunto de dados imutáveis).

for key in meu_nome.items():
    print(key)

#values(): Retorna os valores das chaves.

for key in meu_nome.values():
    print(key)

#keys(): Retorna as chaves.
for key in meu_nome.keys():
    print(key)

print(meu_nome.items())
print(meu_nome.values())
print(meu_nome.keys())
