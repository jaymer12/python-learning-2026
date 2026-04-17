# ================================================
# DAY 9 - Fixed FastAPI + SQLite (CRUD)
# ================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Column, Integer, String, Boolean

# ====================== Database Setup ======================
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)

engine = sa.create_engine("sqlite:///./tasks.db", echo=False)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ====================== FastAPI Setup ======================
app = FastAPI(title="JAY's Todo API - Fixed Version")

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
        from_attributes = True   # This allows ORM objects to be converted

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====================== Endpoints ======================

@app.get("/")
def home():
    return {"message": "Todo API is running (Fixed)"}

# Create Task
@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get All Tasks - FIXED VERSION
@app.get("/tasks/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

# Get Single Task
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

print("✅ Fixed Todo API is ready!")
print("Run: uvicorn day9_fastapi_database:app --reload")