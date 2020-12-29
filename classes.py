from datetime import date

class Book:
  def __init__(self, title, author, genre, reading_date, pages):
    self.title = title
    self.author = author
    self.genre = genre
    self.reading_date = reading_date
    self.pages = pages
  
class Bookcase:
  def __init__(self, books):
    self.books = books
  
  def add_new_book(self, new_book):
    self.books.append(new_book)

  def print(self):
    ind = 1
    for book in self.books:
      print(str(ind) + ". " + book.title + ", by " + book.author)
      ind += 1

  def search_by_parameter(self, title, author, genre):
    return filter(lambda book: (book.title == title or title == "") and (book.author == author or author =="") and (book.genre == genre or genre == ""), self.books)

  def is_empty(self):
    return self.books == []
  
  def sum_pages(self, date_from, date_to):
    som = 0
    try:
      date_from = date.fromisoformat(date_from)
    except:
      date_from = date.min
    try:
      date_to = date.fromisoformat(date_to)
    except:
      date_to = date.max
    for book in self.books:
      book_date = date.fromisoformat(book.reading_date)
      if book_date > date_from and book_date < date_to:
        som += book.pages
    return som