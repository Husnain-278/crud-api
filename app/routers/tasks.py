from fastapi import APIRouter
from app.services import task_service

router = APIRouter(prefix="", tags=["Tasks"])


@router.get("/")
def greetings():
    return task_service.hello_server()