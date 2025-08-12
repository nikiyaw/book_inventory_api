from fastapi import FastAPI
from app.routers import books

app = FastAPI(title="Book Inventory API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Inventory API"}

# Include routers
app.include_router(books.router)