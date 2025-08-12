from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas import Book, BookCreate

router = APIRouter(prefix="/books", tags=["Books"])

books_db = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 3, "title": "Code Complete", "author": "Steve McConnell"},
    {"id": 4, "title": "Design Patterns", "author": "Erich Gamma"},
    {"id": 5, "title": "Refactoring", "author": "Martin Fowler"},
    # Add more sample books if you want
]

next_id = 6

@router.get("/", response_model=list[Book])
def get_books(
    title: Optional[str] = Query(None, description="Filter by book title"),
    author: Optional[str] = Query(None, description="Filter by author name"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=50, description="Number of books per page"),
):
    # Filter by title and author (case insensitive)
    filtered = books_db
    if title:
        filtered = [book for book in filtered if title.lower() in book["title"].lower()]
    if author:
        filtered = [book for book in filtered if author.lower() in book["author"].lower()]

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated = filtered[start:end]

    return paginated

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