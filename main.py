from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import router as auth_router
from routers.tasks import router as tasks_router
import models
from database import engine
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="JAY's Todo API", version="1.0")

origins = [
    "http://localhost:5173",
    "https://python-learning-2026.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to JAY's Todo API ✅",
        "status": "running",
        "docs": "/docs"
    }