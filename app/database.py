import certifi
from pymongo import MongoClient
from .config import MONGO_URI, MONGO_DATABASE

ssl_ca_certs = certifi.where()

client = MongoClient(MONGO_URI, tlsCAFile=ssl_ca_certs)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client[MONGO_DATABASE]
product_collection = db['products']
order_collection = db['orders']
