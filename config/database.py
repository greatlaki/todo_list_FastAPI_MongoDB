import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(
    f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('CLUSTER')}/{os.getenv('COLLECTION')}"
)

db = client.todo_app

collection_name = db['todos_app']
