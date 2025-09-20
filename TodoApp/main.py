from fastapi import FastAPI,Depends,HTTPException,Path
from TodoApp import models
from TodoApp.database import engine,SessionLocal
from TodoApp.models import Todo
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel,Field

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()

    try:
        yield db
    finally:
        db.close

db_dependency =Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title:str = Field(min_length=3)
    description:str = Field(min_length=3 , max_length=100)
    priority:int = Field(gt=0 , lt=6)
    Complete:bool




@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(Todo).all()


@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency, todo_id:int=Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Todo is not found")


@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model =Todo(**todo_request.model_dump())
    
    db.add(todo_model)
    db.commit()