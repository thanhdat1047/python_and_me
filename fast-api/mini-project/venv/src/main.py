from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from data import books_db
from enum import Enum

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    published_year: int
    summary: str
    image: str

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet   = "lenet"

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.get("/books/{id}", response_model=Book)
def get_book_by_id(id: int):
    for book in books_db:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def create_book(book: Book):
    if any(b["id"] == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books_db.append(book.model_dump())
    return book

@app.put("/books/{id}", response_model=Book)
def update_book(id: int, update_book: Book):
    for idx, book in enumerate(books_db):
        if book["id"] == id:
            books_db[idx] == update_book.model_dump()
            return update_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}", status_code=204)
def delete_book(id: int):
    global books_db
    init_len = len(books_db)
    books_db = [book for book in books_db if book["id"] != id]
    if init_len == len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book delete successfully"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "mess": "Deep learning"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "mess": "LeCNN"}
    return {"model_name": model_name, "mess": "RNN"}

    
        
        

        

