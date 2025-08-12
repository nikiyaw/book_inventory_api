from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Books"])

# Example GET endpoint
@router.get("/")
def get_books():
    return [
        {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
        {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"}
    ]