from fastapi import APIRouter
from app.services import task_service

router = APIRouter(prefix="", tags=["Tasks"])


@router.get("/")
def task_api():
    return task_service.task_api_info()


@router.get("/health")
def health():
    return {
        "status": "ok"
    }
    
    
@router.get("/tasks")
def tasks():
    return task_service.list_tasks()


@router.get("/tasks/{task_id}")
def task(task_id: int):
    return task_service.task(task_id)