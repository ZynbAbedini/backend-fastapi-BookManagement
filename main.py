from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Library Management API",
    description="A simple in-memory book management system built with FastAPI",
    version="1.0.0",
)


class Book(BaseModel):
    id: int = Field(..., description="Unique identifier for the book")
    title: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author of the book")
    year: int = Field(..., description="Publication year")


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, description="Title of the book")
    author: str | None = Field(default=None, description="Author of the book")
    year: int | None = Field(default=None, description="Publication year")


# In-memory storage using a dictionary (Hash Map) for O(1) high-performance lookups
books: dict[int, Book] = {
    1: Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
    2: Book(id=2, title="1984", author="George Orwell", year=1949),
    3: Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
}


@app.get("/books", response_model=list[Book], status_code=status.HTTP_200_OK)
def get_books():
    """Retrieve the list of all books."""
    return list(books.values())


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """Add a new book to the library."""
    if book.id in books:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Book with ID {book.id} already exists",
        )
    books[book.id] = book
    return book


@app.get("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
def get_book(id: int):
    """Retrieve a specific book by its ID."""
    book = books.get(id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {id} not found",
        )
    return book


@app.patch("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
def update_book(id: int, book_update: BookUpdate):
    """Partially update a book's information by its ID."""
    book = books.get(id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {id} not found",
        )

    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book, key, value)
    return book


@app.delete("/books/{id}", status_code=status.HTTP_200_OK)
def delete_book(id: int):
    """Delete a specific book by its ID."""
    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {id} not found",
        )

    del books[id]
    return {"message": f"Book with ID {id} deleted successfully"}