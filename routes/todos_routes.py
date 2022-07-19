from fastapi import APIRouter
from config.database import collection_name
from schemas.todos_schemas import *

todo_api_router = APIRouter()


# retrieve
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return todos
