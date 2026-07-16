from fastapi import APIRouter
from app.services import task_service
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import status

router = APIRouter(prefix="", tags=["Tasks"])


@router.get("/", description="Returns the info of this Project")
def task_api():
    return task_service.task_api_info()


@router.get("/health", description="Returns a health of project.")
def health():
    return {
        "status": "ok"
    }
    
    
@router.get("/tasks", description="Returns a list of all available tasks.")
def tasks():
    return task_service.list_tasks()


@router.get("/tasks/{task_id}", description="Returns a single task by its ID.")
def task(task_id: int):
    return task_service.task(task_id)


@router.post("/tasks", description="Creates a new task.")
def create_task(task: TaskCreate):
    return task_service.create_task(task.title)


@router.patch("/tasks/{task_id}", description="Updates the title and/or completion status of a task.")
def update_task(task_id: int, task: TaskUpdate):
    return task_service.update_task(task_id, task)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, description="Deletes a task by its ID.")
def delete_task(task_id: int):
    return task_service.delete_task(task_id)