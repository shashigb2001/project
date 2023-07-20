from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

library = {"users": {1: {"shashi", 22, 9997868631}}, "books": dict(general=10, physics=10, science=10, social=10)}


class User(BaseModel):
    name: str
    age: int
    phone: int


class Book(BaseModel):
    no_of_book: int


@app.get("/library/users")
async def display_details():
    return library["users"]


@app.get("/library/books")
async def book_details():
    return library["books"]


@app.post("/library/users/{user_id}")
async def create_user(user_id: int , user: User):
    if user_id not in library["users"]:
        user_dict = user.dict()
        library["users"][user_id] = user_dict
        return user_dict
    return "userid already exists"


@app.put("/library/users/update/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id in library["users"]:
        user_dict = user.dict()
        library["users"][user_id] = user_dict
        return user_dict
    return "userid not exists"


@app.post("/library/books/{book_name}")
async def add_book(book_name: str, no_of_books: int):
    if book_name not in library["books"]:
        library["books"][book_name] = no_of_books
        return library["books"]
    return "book already added"


@app.delete("/library/users/del/{user_id}")
async def del_user(user_id: int):
    if user_id in library["users"]:
        del library["users"][user_id]
        return "user id deleted"
    return "userid not exists"


@app.delete("/library/books/del/{book_name}")
async def del_user(book_name: str):
    if book_name in library["books"]:
        del library["books"][book_name]
        return "book deleted"
    return "book not exists"
