# main.py
from fastapi import FastAPI
from routers.tasks import router as tasks_router

app = FastAPI(title="JAY's Todo API", version="1.0")

# Include the tasks router
app.include_router(tasks_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to JAY's Structured Todo API - Day 10 ✅",
        "status": "running",
        "docs": "/docs"
    }