from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float


items = [
    {"id": 1, "name": "Notebook", "price": 2.5},
    {"id": 2, "name": "Backpack", "price": 24.99},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API."}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    items.append(item.model_dump())
    return {"message": "Item added successfully.", "item": item}


# Run with:
# uvicorn starter-code:app --reload