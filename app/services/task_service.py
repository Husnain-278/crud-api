from app.data.storage import tasks
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.task import TaskUpdate
from app.data.storage import get_all_tasks, get_task_by_id


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
    new_id = max((task["id"] for task in tasks), default=0) + 1
    task_to_append = {
        "id": new_id,
        "title": title,
        "done": False
    }
    tasks.append(task_to_append)
    return JSONResponse(
        content=task_to_append,
        status_code=status.HTTP_201_CREATED,
    )
    
    

#Update task
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            
            if update.title is not None:
                task["title"] = update.title
            
            if update.done is not None:
                task["done"] =  update.done
                
            return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )
    
    

#Delete a task
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )