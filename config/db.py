from pymongo import MongoClient


Mongo_URI = "mongodb+srv://shakir:Cc118328@clusters.z5zswcg.mongodb.net/"

conn = MongoClient(Mongo_URI)

docs = conn.notes.notes.find({'title': 'hi '})
for c in docs:
    print(c)