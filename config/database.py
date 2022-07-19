import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(
    f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@cluster0.ewhet.mongodb.net/?retryWrites=true&w=majority"
)

db = client.todo_app

collection_name = db['todos_app']
