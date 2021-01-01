from classes import Book
from classes import Bookcase
from datetime import date

def test_book():
  book1 = Book("title1", "author1", "genre1 genre4", date(2021, 1, 1), 100)
  book2 = Book("title2", "author2", "genre2 genre4 genre5", date(2021, 4, 1), 200)
  book3 = Book("title3", "author3", "genre3 genre5", date(2019, 1, 2), 300)
  assert book1.title == "title1", "test failed book1 title"
  assert book2.title == "title2", "test failed book2 title"
  assert book3.title == "title3", "test failed book3 title"
  assert book1.author == "author1", "test failed book1 author"
  assert book2.author == "author2", "test failed book2 author"
  assert book3.author == "author3", "test failed book3 author"
  assert book1.genre == ["genre1", "genre4"], "test failed book1 genre"
  assert book2.genre == ["genre2", "genre4", "genre5"], "test failed book2 genre"
  assert book3.genre == ["genre3", "genre5"], "test failed book3 genre"
  assert book1.reading_date == date(2021, 1, 1), "test failed book1 date"
  assert book2.reading_date == date(2021, 4, 1), "test failed book2 date"
  assert book3.reading_date == date(2019, 1, 2), "test failed book3 date"
  assert book1.pages == 100, "test failed book1 pages"
  assert book2.pages == 200, "test failed book2 pages"
  assert book3.pages == 300, "test failed book3 pages"
