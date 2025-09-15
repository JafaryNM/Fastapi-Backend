from fastapi import FastAPI

app = FastAPI()

BOOOKS = [
    {'title':'Title One', 'author':'Authour 1', 'categories':'science'},
    {'title':'Title Two', 'author':'Authour 2', 'categories':'arts'},
    {'title':'Title Three', 'author':'Authour 3', 'categories':'physics'},
    {'title':'Title Four', 'author':'Authour 4', 'categories':'agriculture'},
    {'title':'Title Five', 'author':'Authour 5', 'categories':'geography'},
    {'title':'Title Six', 'author':'Authour 6', 'categories':'english liturature'},
]

@app.get("/books")
async def first_app():
    return BOOOKS


@app.get('/books/mybooks')
async def read_all_books():
    return {'book-title':'My favorate books'}

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOOKS:
        if book.get('title').casefold()== book_title.casefold():
            return book
