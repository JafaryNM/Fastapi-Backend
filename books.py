from fastapi import FastAPI

app = FastAPI()

BOOOKS = [
    {'title':'Title First', 'author':'Authour 1', 'categories':'science'},
    {'title':'Title Two', 'author':'Authour 2', 'categories':'arts'},
    {'title':'Title Three', 'author':'Authour 3', 'categories':'physics'},
    {'title':'Title Four', 'author':'Authour 4', 'categories':'agriculture'},
    {'title':'Title Five', 'author':'Authour 5', 'categories':'geography'},
    {'title':'Title Six', 'author':'Authour 6', 'categories':'english liturature'},
]

@app.get("/books")

async def first_app():
    return BOOOKS