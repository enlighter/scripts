from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.psva
print(db['drugs'])
inserted_id = db['drugs'].insert_one(json.loads('{ drug_id : 1, name : "Lepirudin" }')).inserted_id

print(inserted_id)

client.close()