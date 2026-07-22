
# 🚀 Task CRUD API

A simple **Task CRUD API** built with **FastAPI** and **SQLite**.

This project demonstrates a complete CRUD API while following a layered architecture:

**Router → Service → Storage → SQLite**

The application originally used an in-memory list and was migrated to **SQLite** for persistent data storage.

---

# ✨ Features

- List all tasks
- Get a single task by ID
- Create a new task
- Update an existing task
- Delete a task
- Persistent SQLite storage
- Interactive Swagger UI
- Automatic OpenAPI documentation

---

# 🛠 Tech Stack

- Python 3.12+
- FastAPI
- SQLite (`sqlite3`)
- Uvicorn
- Pydantic
- uv (Package Manager)

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/task-crud-api.git
cd task-crud-api
```

## 2. Create a virtual environment

```bash
uv venv
```

## 3. Activate it

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

## 4. Install dependencies

```bash
uv sync
```

## 5. Run the application

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📚 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Project information |
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a task |
| PATCH | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

# 🗄 Database

The project now uses **SQLite** for persistent storage.

Database location:

```
app/data/tasks.db
```

On startup the application:

- Creates the database if it does not exist.
- Creates the `tasks` table automatically.
- Inserts sample tasks only on the first run.

---

# 🔍 Exploring SQLite

Commands used during Stage 4:

```sql
.tables
.schema tasks
.headers on
.mode column
SELECT * FROM tasks;
SELECT COUNT(*) FROM tasks;
SELECT * FROM tasks WHERE id = 1;
SELECT * FROM tasks WHERE done = 1;
SELECT * FROM tasks ORDER BY id DESC;
```

---

# 📖 What I Learned

- Connecting to SQLite using Python's `sqlite3` module.
- Creating tables with SQL.
- Using parameterized SQL queries (`?`) to prevent SQL injection.
- Implementing CRUD operations with SQL.
- Using `fetchone()` and `fetchall()`.
- Using `sqlite3.Row` to access columns by name.
- Structuring a FastAPI project using Router → Service → Storage architecture.
- Inspecting a SQLite database using the SQLite command-line tool.

---

# 📸 Screenshots

## Swagger UI

![Swagger UI](images/Swagger_ui_screenshot.png)

---

## cURL Output

![cURL Output](images/curl_screenshot.png)

---

# 📁 Project Structure

```text
app/
├── data/
│   ├── storage.py
│   └── tasks.db
├── routers/
│   └── tasks.py
├── schemas/
│   └── task.py
├── services/
│   └── task_service.py
└── main.py
```

---

# 🚀 Future Improvements

- Add pagination.
- Add search functionality.
- Add authentication.
- Add automated tests.
- Migrate to SQLModel or SQLAlchemy for larger applications.

---

# License

This project was created for learning FastAPI, REST APIs, and SQLite.
