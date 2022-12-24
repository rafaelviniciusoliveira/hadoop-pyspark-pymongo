from pymongo import MongoClient


def filtrarDados(querie: dict) -> list:
  dados_filtrados = base.find(querie)

  return list(dados_filtrados)


client = MongoClient("mongodb://mongo-teste", 27017, authSource='admin&readPreference=secondary&directConnection=true&ssl=false')
db = client['discentes_data']
base = db['Discentes']

qtd_mulheres = len(filtrarDados({"sexo":"F"}))
qtd_homens = len(filtrarDados({"sexo":"M"}))
porcentagem_mulheres = qtd_mulheres/(qtd_mulheres+qtd_homens)
print("\n")
print(f'No ano de 2022 a porcentagem de mulheres ingressantes foi de {int(porcentagem_mulheres*100)}%')
print("\n")