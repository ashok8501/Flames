from pymongo import MongoClient

MONGO_URL = "mongodb+srv://ashokreddy15:8501877820@cluster0.wowtf41.mongodb.net"

client = MongoClient(MONGO_URL)
db = client["flames_db"]
collection = db["results"]