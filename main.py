from fastapi import FastAPI

app = FastAPI(title="Book Inventory API")

# Health check route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Inventory API"}

# Example GET endpoint
@app.get("/books")
def get_books():
    return [
        {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
        {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"}
    ]