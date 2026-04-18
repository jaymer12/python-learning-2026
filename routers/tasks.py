from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import schemas
from database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Create Task
@router.post("/", response_model=schemas.TaskResponse)
def create_task(task:schemas.TaskCreate, db:Session= Depends(get_db)):
    return crud.create_task(db, task)

# Get All tasks
@router.get("/", response_model=List[schemas.TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

#Get Single Task
@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

#Update task( Title, description, or Mark as Done)
@router.put("/{task_id}", response_model= schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

# Delete task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} is deleted successfully"}