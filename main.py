
from typing import Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Book:
    __slots__ = ["id", "name", "author", "year", "count"]
    def __init__(self, id: int, name: str, author: str, year: str, count: int):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.count = count

books = [Book(1, "Война и мир", "Лев Толстой", "1834", 3),
         Book(2, "Евгений Онегин", "Пушкин", "1812", 2),
         Book(3, "Три сестры", "Чехов", "1878", 9)]



@app.get("/")
def index(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "books": books})

@app.get("/books/{book_id}")
def read_item(request: Request, book_id: int):
    target_book = None
    for b in books:
        if b.id == book_id:
            target_book = b
            break
    if not target_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return templates.TemplateResponse("item.html", {"request": request, "book": target_book})


