from fastapi import FastAPI,Body

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
    

# Post request method

@app.post("/books/create_books")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Put request method to update book 
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
       if BOOKS[i].get("title").casefold()==update_book.get('title').casefold():
           BOOKS[i]=update_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()== book_title.casefold():
            BOOKS.pop(i)
            break