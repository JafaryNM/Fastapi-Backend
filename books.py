from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author Two", "category": "science"},
    {"title": "Title Two", "author": "Author  Two", "category": "science"},
    {"title": "Title Three", "author": "Author 3", "category": "math"},
    {"title": "Title Four", "author": "Author 4", "category": "agriculture"},
    {"title": "Title Five", "author": "Author 5", "category": "geography"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]

# Fetching All parameters

@app.get("/all-books")
async def first_app():
    return BOOKS


@app.get('/books/mybooks')
async def read_all_books():
    return {'book-title':'My favorate books'}


# Fetching By Parameters

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()== book_title.casefold():
            return book


# By Query Category Parameters

@app.get('/books')
async def ready_category_by_query(category:str):
     books_to_return=[]
     for book in BOOKS:
         if book.get('category').casefold()== category.casefold():
             books_to_return.append(book)
     return books_to_return




@app.get("/books-author/{author}")
async def read_books_by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('author').casefold() == author.casefold() and 
            book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return
    
