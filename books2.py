from fastapi import FastAPI,Path
from pydantic import BaseModel,Field,ConfigDict
from typing  import Optional,List

app = FastAPI()

class Book:
    id:str
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self, id , title, author, description, rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id:Optional[int]= Field(description="Id is not needed on created", default=None)
    title:str= Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length=100)
    rating:int = Field(gt=-0 , lt= 6)
    published_date : int=Field(gt=1999,lt=2031)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "A new book",
                    "author": "codewithjeff",
                    "description": "A new description of the book",
                    "rating": 5,
                    'published_date':2021
                }
            ]
        }
    )
 

    
BOOKS: List[Book] = [
    Book(id=1, title="Computer Science", author="Jafary Mdegela",
         description="This is good book for computer programming", rating=5, published_date=2003),
    Book(id=2, title="Next frontend book", author="John Samson",
         description="This is book for frontend-framework", rating=4,published_date=2020),
    Book(id=3, title="React js", author="Someone",
         description="This is good book for frontend", rating=5,published_date=2003),
]

@app.get("/books")
async def read_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books-rating")
async def reading_book_by_rating(book_rating:int):
    books_to_return = []
    for book in BOOKS :
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books-published-date")
async def read_books_by_published_date(published_date:int):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==published_date:
            books_to_return.append(book)
    return books_to_return



@app.post('/books/create_books')
async def create_books(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(new_book)
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
     book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id +1
     return book

@app.put('/books/update_book')
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id== book.id:
            BOOKS[i]= book


@app.delete("/books/{book_id}")
async def delete_book(book_id:int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

