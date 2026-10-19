
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task Manager API")

# Temporary in-memory storage
tasks = {}
next_id = 1


# Data required to create a task
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""
    completed: bool = False


# Data allowed when updating a task
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    completed: bool | None = None


# Home route
@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


# Create a new task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        **task.model_dump()
    }

    tasks[next_id] = new_task
    next_id += 1

    return new_task


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return list(tasks.values())


# Get one task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# Update a task
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, updates: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    changes = updates.model_dump(exclude_unset=True)
    tasks[task_id].update(changes)

    return tasks[task_id]


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }
