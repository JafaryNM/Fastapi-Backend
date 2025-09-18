from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing  import Optional

app = FastAPI()

class Book:
    id:str
    title:str
    author:str
    description:str
    rating:int

    def __init__(self, id , title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id:Optional[int]= None
    title:str= Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length=100)
    rating:int = Field(gt=-0 , lt= 6)


BOOKS = [
    Book(1,"Computer Science", "Jafary Mdegela", "This is good book for computer programmng", 5),
    Book(2,"Next frontend boo", "John Samson", "This is book for frontend-framework", 4),
    Book(3,"React js", "Book for reactjs", "This is good book for frontendbook", 5),
    Book(4,"Django Backend", "Stephen Grider", "Good for backend full stack", 3),
    Book(5,"Flask Api Developement", "John Doe", "This is for backend developement", 3),
    Book(6,"Backend Nodejs", "Juma Tone", "This is Flask Testing", 3)
]

@app.get("/books")
async def read_books():
    return BOOKS


@app.post('/books/create_books')
async def create_books(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(new_book)
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
     book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id +1
     return book