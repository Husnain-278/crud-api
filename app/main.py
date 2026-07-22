from fastapi import FastAPI
from app.routers import tasks
from app.data.storage import initialize_database

app = FastAPI(
    title="Task CRUD API",
    description="A simple CRUD API for managing tasks.",
    version="1.0.0",
)

#Initialize the db
initialize_database()

app.include_router(tasks.router)

