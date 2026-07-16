from app.data.storage import tasks
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status


def task_api_info():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/","/health","/tasks"]
    }
    
    
#Return all tasks
def list_tasks():
    return tasks


#Return task by id
def task(id):
    for task in tasks:
       if task["id"] == id:
           return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {id} not found"
    )
    
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