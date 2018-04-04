from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.psva

data_list = []

with open('diseases_mongo_json.txt') as diseases_file:
    data_list = diseases_file.readlines()

for line in data_list:
    line = line[:-2]
    single_entry_dict = json.loads(line)
    print(single_entry_dict)

    inserted_id = db['diseases'].insert_one(single_entry_dict).inserted_id
    print(inserted_id)

client.close()
print("closed connection")
