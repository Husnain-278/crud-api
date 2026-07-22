from app.data.storage import tasks
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.task import TaskUpdate
from app.data.storage import get_all_tasks, get_task_by_id, create_task as db_create_task
from app.data.storage import (
    update_task as db_update_task,
    delete_task as db_delete_task,
)


def task_api_info():
    return {
        "name": "Task API",
        "version": "1.0.0",
        "endpoints": ["/","/health","/tasks"]
    }
    
    
#Return all tasks or filter by done
def list_tasks(done: bool | None = None):
    tasks = get_all_tasks()
    if done is None:
        return tasks
    
    return [task for task in tasks if task["done"] == done]


#Return task by id
def task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )

    return task
    
#Create Task
def create_task(title: str):
    if not title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty",
        )
    
    task = db_create_task(title)

    return JSONResponse(
        content=task,
        status_code=status.HTTP_201_CREATED,
    )
        
    
    

#Update task
def update_task(task_id: int, update: TaskUpdate):
    task = db_update_task(
        task_id,
        update.title,
        update.done,
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )

    return task
    

#Delete a task
def delete_task(task_id: int):
    deleted = db_delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )