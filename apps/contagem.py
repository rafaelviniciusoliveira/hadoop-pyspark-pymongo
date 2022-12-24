from pymongo import MongoClient
import math
client = MongoClient("mongodb://mongo-teste", 27017, authSource='admin&readPreference=secondary&directConnection=true&ssl=false')
db = client['discentes_data']
collection = db['Discentes']

dict_contagem = {}
dados = list(collection.find())

for i in dados:
  if dict_contagem.get(i['forma_ingresso'], None) is None:
    dict_contagem[i['forma_ingresso']]=1
  else:
    dict_contagem[i['forma_ingresso']]+=1

print("\n")
for i in dict_contagem.keys():
  if type(i)!= float:
    print(f'{i}: {dict_contagem[i]}')
print("\n")