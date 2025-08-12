from fastapi import FastAPI
from app.routers import books, auth

app = FastAPI(title="Book Inventory API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Inventory API"}

app.include_router(auth.router)
app.include_router(books.router)