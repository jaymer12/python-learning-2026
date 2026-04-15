# ================================================
# DAY 9 - FastAPI + SQLite Database (CRUD)
# ================================================
# Goal: Learn how to connect FastAPI with Database

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean

# ====================== Database Setup ======================
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)

# Create database engine
engine = sa.create_engine("sqlite:///./tasks.db", echo=False)
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ====================== FastAPI Setup ======================
app = FastAPI(
    title="JAY's Todo API",
    description="Day 9 - FastAPI with SQLite Database"
)

# Pydantic Models
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool

    class Config:
        from_attributes = True

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====================== API Endpoints ======================

@app.get("/")
def home():
    return {"message": "Todo API is running - Day 9"}

# Create a new task (POST)
@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db = get_db()):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks (GET)
@app.get("/tasks/", response_model=List[TaskResponse])
def get_all_tasks(db = get_db()):
    tasks = db.query(Task).all()
    return tasks

# Get single task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db = get_db()):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update task (PUT)
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate, db = get_db()):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = updated_task.title
    task.description = updated_task.description
    db.commit()
    db.refresh(task)
    return task

# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db = get_db()):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted successfully"}

print("✅ Todo API with Database is ready!")
print("Run this command to start:")
print("   uvicorn day9_fastapi_database:app --reload")
print("\nOpen in browser:")
print("   → http://127.0.0.1:8000/docs")