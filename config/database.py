import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@cluster0."
                     f"ewhet.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name = db['todos_app']
