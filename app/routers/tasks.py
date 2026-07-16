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