from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
host = os.getenv("HOSTNAME") #truy xuất giá trị của biến môi trường HOSTNAME
client = MongoClient(host)
db = client['Group11']
users_collection = db['users']
expenses_collection = db['expenses']


user=users_collection.find_one({'username': "Thien"})
print(user)