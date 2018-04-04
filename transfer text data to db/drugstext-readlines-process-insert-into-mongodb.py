from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.psva

data_list = []

with open('drug_mongo_json.txt') as drugs_file:
    data_list = drugs_file.readlines()

for line in data_list:
    entry = line.split(',')
    entry = entry[0].strip('{').split(':') + entry[1].strip('}').split(':')
    entry = [e.strip().strip('"') for e in entry]

    single_entry_dict = dict()
    single_entry_dict[entry[0]] = int(entry[1])
    single_entry_dict[entry[2]] = entry[3]
    print(single_entry_dict)

    inserted_id = db['drugs'].insert_one(single_entry_dict).inserted_id
    print(inserted_id)

client.close()
print("closed connection")
