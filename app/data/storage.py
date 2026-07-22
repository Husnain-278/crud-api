import sqlite3
from pathlib import Path
from fastapi import HTTPException
from fastapi import status

DB_PATH = Path(__file__).parent / "tasks.db"


def initialize_database():
    #Open or create the db
    connection = sqlite3.connect(DB_PATH)
    cursor =   connection.cursor()
    
    #Create a tasks table of it does not exist
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks (
                       id INTEGER PRIMARY KEY,
                       title TEXT NOT NULL,
                       done BOOLEAN NOT NULL
                   )
                   """)
    
    
    #Check whether the table already contains data
    cursor.execute("SELECT COUNT(*) FROM tasks")
    task_count = cursor.fetchone()[0]
    
    #Seed the db only on the first run
    if task_count == 0:
        sample_tasks = [
            ("Buy groceries", False),
            ("Complete FastAPI assignment", True),
            ("Learn SQLite", False),
        ]
        
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            sample_tasks,
        )
        
    #Save changes and close the connection
    connection.commit()
    connection.close()
    
    
def get_all_tasks():
    connection = sqlite3.connect(DB_PATH)    
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append({
            "id": row['id'],
            "title": row["title"],
            "done": bool(row["done"]),
        })
    
    connection.close()
    return tasks    
    
    
def get_task_by_id(task_id: int):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,),
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
    }
    
    

def create_task(title: str):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    
    cursor = connection.cursor()
    
    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (title, False),
    )
    connection.commit()
    task_id = cursor.lastrowid
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,),
    )
    row = cursor.fetchone()
    connection.close()
    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
    }

    
    

def update_task(task_id: int, title: str | None = None, done: bool | None = None):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,),
    )

    row = cursor.fetchone()

    if row is None:
        connection.close()
        return None

    new_title = title if title is not None else row["title"]
    new_done = done if done is not None else bool(row["done"])

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, done = ?
        WHERE id = ?
        """,
        (new_title, new_done, task_id),
    )

    connection.commit()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,),
    )

    row = cursor.fetchone()

    connection.close()

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
    }



def delete_task(task_id: int):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,),
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted > 0

    

tasks = [
    {
        "id": 1,
        "title": "Demo task 1",
        "done": False,
    },
    {
        "id": 2,
        "title": "Demo task 2",
        "done": True,
    },
    {
        "id": 3,
        "title": "Demo task 1",
        "done": False,
    },
]


