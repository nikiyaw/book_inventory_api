from fastapi import APIRouter, HTTPException
from app.schemas import Book, BookCreate

router = APIRouter(prefix="/books", tags=["Books"])

# Temporary in-memory database
books_db = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"}
]
next_id = 3

@router.get("/", response_model=list[Book])
def get_books():
    return books_db

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    global next_id
    new_book = {"id": next_id, **book.dict()}
    books_db.append(new_book)
    next_id += 1
    return new_book

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: BookCreate):
    for book in books_db:
        if book["id"] == book_id:
            book.update(updated_book.dict())
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Book not found")