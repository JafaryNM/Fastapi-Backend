from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_app():
    return {"message":"Jafary fast api"}