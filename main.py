from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Library Management API",
    description="A simple in-memory book management system built with FastAPI",
    version="1.0.0",
)


class Book(BaseModel):
    id: int = Field(gt=0, description="Unique identifier for the book")
    title: str = Field(min_length=1, description="Title of the book")
    author: str = Field(min_length=1, description="Author of the book")
    year: int = Field(gt=0, description="Publication year")

class BookUpdate(BaseModel):
    title: str | None = Field(default=None, description="Title of the book", min_length=1)
    author: str | None = Field(default=None, description="Author of the book", min_length=1)
    year: int | None = Field(default=None, description="Publication year", gt=0)


# In-memory storage with initial sample data
books: list[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
    Book(id=2, title="1984", author="George Orwell", year=1949),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
]


@app.get("/books", response_model=list[Book], status_code=status.HTTP_200_OK)
def get_books():
    """Retrieve the list of all books."""
    return books


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """Add a new book to the library."""
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Book with ID {book.id} already exists",
            )
    books.append(book)
    return book


@app.get("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
def get_book(id: int):
    """Retrieve a specific book by its ID."""
    for book in books:
        if book.id == id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with ID {id} not found",
    )


@app.patch("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
def update_book(id: int, book_update: BookUpdate):
    """Partially update a book's information by its ID."""
    for book in books:
        if book.id == id:
            update_data = book_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(book, key, value)
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with ID {id} not found",
    )


@app.delete("/books/{id}", status_code=status.HTTP_200_OK)
def delete_book(id: int):
    """Delete a specific book by its ID."""
    for book in books:
        if book.id == id:
            books.remove(book)
            return {"message": f"Book with ID {id} deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with ID {id} not found",
    )