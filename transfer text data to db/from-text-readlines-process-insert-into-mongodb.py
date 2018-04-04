from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.psva

data_list = []

with open('drug_mongo_json.txt') as drugs_file:
	data_list = drugs_file.readlines()
inserted_id = db['drugs'].insert_one(json.loads('{ drug_id : 1, name : "Lepirudin" }')).inserted_id

print(inserted_id)

client.close()