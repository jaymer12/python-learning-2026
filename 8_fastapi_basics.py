# ================================================
# DAY 8 - My First FastAPI Application
# ================================================
# Goal: Learn FastAPI basics

from fastapi import FastAPI #  Main framework to build the API
from pydantic import BaseModel # Used to define the structure of data (like a form)
from typing import Optional # Means a field can be empty or None

# Create FastAPI app This creates your API application. Think of it as starting a new "shop".
app = FastAPI(
    title="JAY's FastAPI Learning App",
    description="Day 8 - Building my first backend API",
    version="1.0"
)

# ==================== GET Endpoints ====================

@app.get("/")
def read_root():
    return {
        "message": "Hello from JAY's First FastAPI!",
        "status": "success",
        "day": 8,
        "location": "Regina, Saskatchewan"
    }

@app.get("/hello")
def hello_user(name: str = "Guest"):
    return {
        "message": f"Hello {name}! Welcome to my API.",
        "city": "Regina"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "query": q,
        "message": f"You requested item number {item_id}"
    }

# ==================== POST Endpoint with Data Validation ====================

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
def create_item(item: Item):
    total = item.price + (item.tax or 0)
    return {
        "message": "Item created successfully!",
        "item": item,
        "total_price_with_tax": total
    }

# Status endpoint
@app.get("/status")
def get_status():
    return {
        "status": "API is running",
        "developer": "JAY",
        "learning_day": 8
    }


print("✅ FastAPI is ready!")
print("Run this command in terminal:")
print("   uvicorn day8_fastapi_basics:app --reload")
print("\nOpen these URLs in browser:")
print("   → http://127.0.0.1:8000")
print("   → http://127.0.0.1:8000/docs   ← Best one!")