# python -m venv venv
# ./venv/Scripts/activate.bat
# pythom -m install -U upgrade pip
# pip install fastapi[all]
# pip install -U autopep8
# uvicorn Librarian.main:app --reload

# importing required libraries for API developement

# Fastapi libraries required for API 
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from typing import Optional
# pydantic schema defination library 
from pydantic import BaseModel
# random package to generate random numbers
from random import randrange

# creating instance of FastAPI()
app = FastAPI()

# defining schema using pydantic 
class Book(BaseModel):
    title: str
    content: str
    id: Optional[int]=None
    published: Optional[bool]=True
    rating: Optional[int]=None

# my_books library dataset as list of dictionary
my_books = [{"title":"Book1","content":"Content1","id":1},
            {"title":"Book2","content":"Content2","id":2}]

def find_book_by_id(id: int):
    for i in my_books:
        if i["id"] == id:
            return i

def find_id_of_book(id: int):
    for i,n in enumerate(my_books):
        if n["id"] == id:
            return i

# Handling Create function in CRUD 
@app.post("/books")
def create_books(book: Book, status_code=status.HTTP_201_CREATED):
    book_dict = book.dict()
    if book_dict["id"] == None:
        book_dict["id"] = randrange(1,1000000)
    my_books.append(book_dict)
    return {"data": book_dict}

# Handling Read Function of CRUD
@app.get("/books")
def get_books():
    return {"data": my_books}

# Handling Read Function of CRUD
@app.get("/books/{id}")
def get_book_by_id(id: int):
    book = find_book_by_id(id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"data": book}

#Handling Update Function of CRUD
@app.put("/books/{id}")
def update_books(id: int, book: Book, response: Response):
    index = find_id_of_book(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    book_dict = book.dict()
    book_dict["id"] = id
    my_books[index] = book_dict
    return {"data": book_dict}

#Handling Delete Function of CRUD
@app.delete("/books/{id}")
def delete_books(id: int, response: Response, status_code=status.HTTP_204_NO_CONTENT):
    index = find_id_of_book(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"data": my_books.pop(index)}
    

