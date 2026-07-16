from fastapi import APIRouter
from app.services import task_service
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import status

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


@router.post("/tasks")
def create_task(task: TaskCreate):
    return task_service.create_task(task.title)


@router.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    return task_service.update_task(task_id, task)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    return task_service.delete_task(task_id)