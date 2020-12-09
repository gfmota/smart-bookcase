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
    self.books.push(new_book)

  def search_by_parameter(self, parameter, value):
    return filter(lambda book: getattr(book, parameter) == value, self.books)