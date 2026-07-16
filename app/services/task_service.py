from app.data.storage import tasks
from fastapi import HTTPException
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
        