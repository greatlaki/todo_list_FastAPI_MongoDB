from fastapi import APIRouter

from models.todos_model import Todo
from config.database import collection_name
from schemas.todos_schemas import todos_serializer, todo_serializer

todo_api_router = APIRouter()


# retrieve
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return todos


@todo_api_router.get("/{id}")
async def get_todo(id: str):
    return todos_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@todo_api_router.post("/")
async def create_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    return todos_serializer(collection_name.find({"_id": _id.inserted_id}))
