from pymongo import MongoClient

MONGO_URL = "mongodb+srv://ashokreddy:9347235648@cluster0.pyexy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)
db = client["flames_db"]
collection = db["results"]