from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.psva

data_list = []

with open('investigation_mongo_json.txt') as investigations_file:
    data_list = investigations_file.readlines()

for line in data_list:
    line = line[:-2]
    print(line)
    single_entry_dict = json.loads(line)
    print(single_entry_dict)

    inserted_id = db['investigations'].insert_one(single_entry_dict).inserted_id
    print(inserted_id)

client.close()
print("closed connection")
