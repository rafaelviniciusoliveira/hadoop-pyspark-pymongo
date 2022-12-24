import pandas as pd
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://mongo-teste", 27017, authSource='admin&readPreference=secondary&directConnection=true&ssl=false')
    dataset = pd.read_csv('hdfs://node-master:9000/user/root/dataset/discentes.csv', sep=";")
    dict = dataset.to_dict(orient="records")
    db = client['discentes_data']
    collection = db['Discentes']
    collection.insert_many(dict)