from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
  {"title": "Title One", "author": "Author One", "category": "science"},
  {"title": "Title Two", "author": "Author One", "category": "math"},
  {"title": "Title Three", "author": "Author Two", "category": "science"},
  {"title": "Title Four", "author": "Author Four", "category": "history"},
  {"title": "Title Five", "author": "Author One", "category": "math"}
]

@app.get("/books")
def get_all_books():
  return BOOKS

@app.get("/books/{book_title}")
def get_book(book_title: str):
  for book in BOOKS:
    if book.get('title').casefold() == book_title.casefold():
      return book
    
@app.get("/books/")
def get_book_category(category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('category').casefold() == category.casefold():
      books_to_return.append(book)

  return books_to_return

@app.get("/books/{book_author}/")
async def get_book_author_and_category_by_query(book_author: str, category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
      books_to_return.append(book)

  return books_to_return

@app.post("/books/create_book")
async def post_new_book(new_book=Body()):
  BOOKS.append(new_book)

@app.put("/books/update_book")
async def put_book(updated_book=Body()):
  for i in range(len(BOOKS)):
    if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
      BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title = str):
  for i in range(len(BOOKS)):
    if BOOKS[i].get('title').casefold() == book_title.casefold():
      BOOKS.pop(i)
      break
