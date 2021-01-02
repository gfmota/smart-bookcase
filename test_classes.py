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

def test_bookcase():
  book1 = Book("title1", "author1", "genre1 genre4", date(2021, 1, 1), 100)
  book2 = Book("title2", "author2", "genre2 genre4 genre5", date(2021, 4, 1), 200)
  book3 = Book("title3", "author3", "genre3 genre5", date(2019, 1, 2), 300)
  book4 = Book("title4", "author4", "genre1 genre2", date(2019, 10, 27), 400)
  
  bookcase1 = Bookcase([book1, book2, book3])
  bookcase2 = Bookcase([book1, book3])
  bookcase3 = Bookcase([book1])
  bookcase4 = Bookcase([])
  
  assert bookcase1.books == [book1, book2, book3], "test failed bookcase1 books"
  assert bookcase2.books == [book1, book3], "test failed bookcase2 books"
  assert bookcase3.books == [book1], "test failed bookcase3 books"
  assert bookcase4.books == [], "test failed bookcase4 books"
  
  assert bookcase1.search_by_parameter("title1", "author1", "genre1") == [book1], "test failed bookcase1 search_by_parameter book1"
  assert bookcase1.search_by_parameter("title1", "author1", "genre2") == [], "test failed bookcase1 search_by_parameter no match"
  assert bookcase1.search_by_parameter("", "", "") == [book1, book2, book3], "test failed bookcase1 search_by_parameter empty"
  assert bookcase2.search_by_parameter("title1", "", "genre1") == [book1], "test failed bookcase2 search_by_parameter book1"
  assert bookcase2.search_by_parameter("title2", "author2", "") == [], "test failed bookcase2 search_by_parameter no match"
  assert bookcase3.search_by_parameter("title1", "", "") == [book1], "test failed bookcase3 search_by_parameter book1"
  assert bookcase3.search_by_parameter("", "author3", "") == [], "test failed bookcase3 search_by_parameter no match"
  assert bookcase3.search_by_parameter("", "", "") == [book1], "test failed bookcase3 search_by_parameter empty"
  assert bookcase4.search_by_parameter("", "", "") == [], "test failed bookcase4 search_by_parameter empty"
  assert bookcase4.search_by_parameter("title1", "author2", "genre3") == [], "test failed bookcase4 search_by_parameter no"
  
  assert bookcase1.is_empty() == 0, "test failed bookcase1 is_empty"
  assert bookcase2.is_empty() == 0, "test failed bookcase2 is_empty"
  assert bookcase3.is_empty() == 0, "test failed bookcase3 is_empty"
  assert bookcase4.is_empty() == 1, "test failed bookcase4 is_empty"

  assert bookcase1.sum_pages("", "") == 600, "test failed bookcase1 sum_pages all time"
  assert bookcase1.sum_pages("2021-01-01", "2021-05-13") == 300, "test failed bookcase1 sum_pages year"
  assert bookcase1.sum_pages("2021-02-01", "2021-05-13") == 200, "test failed bookcase1 sum_pages month"
  assert bookcase1.sum_pages("2020-01-01", "2020-12-31") == 0, "test failed bookcase1 sum_pages empty time"
  assert bookcase2.sum_pages("", "") == 400, "test failed bookcase1 sum_pages all time"
  assert bookcase2.sum_pages("2021-01-01", "2021-05-13") == 100, "test failed bookcase2 sum_pages year"
  assert bookcase2.sum_pages("2020-01-01", "2020-12-31") == 0, "test failed bookcase2 sum_pages empty time"
  assert bookcase3.sum_pages("", "") == 100, "test failed bookcase1 sum_pages all time"
  assert bookcase3.sum_pages("2020-01-01", "2020-12-31") == 0, "test failed bookcase3 sum_pages empty time"
  assert bookcase4.sum_pages("", "") == 0, "test failed bookcase1 sum_pages all time"

  assert bookcase1.order_by_parameter("title").books == bookcase1.order_by_parameter("author").books == [book1, book2, book3], "test failed bookcase1 order_by_parameter title and author"
  assert bookcase1.order_by_parameter("reading_date").books == [book3, book1, book2], "test failed bookcase1 order_by_parameter date"
  assert bookcase2.order_by_parameter("title").books ==  bookcase2.order_by_parameter("author").books == [book1, book3], "test failed bookcase2 order_by_parameter title and author"
  assert bookcase2.order_by_parameter("reading_date").books == [book3, book1], "test failed bookcase2 order_by_parameter date"
  assert bookcase3.order_by_parameter("title").books == bookcase3.order_by_parameter("author").books == bookcase3.order_by_parameter("reading_date").books == [book1], "test failed bookcase3 order_by_parameter"
  assert bookcase4.order_by_parameter("title").books == bookcase4.order_by_parameter("author").books == bookcase4.order_by_parameter("reading_date").books == [], "test failed bookcase4 order_by_parameter"

  bookcase1.add_new_book(book4)
  bookcase2.add_new_book(book4)
  bookcase3.add_new_book(book4)
  bookcase4.add_new_book(book4)

  assert bookcase1.books == [book1, book2, book3, book4], "test failed bookcase1 books after add_new_book"
  assert bookcase2.books == [book1, book3, book4], "test failed bookcase2 books after add_new_book"
  assert bookcase3.books == [book1, book4], "test failed bookcase3 books after add_new_book"
  assert bookcase4.books == [book4], "test failed bookcase4 books after add_new_book"

  assert bookcase1.search_by_parameter("title4", "author4", "genre1") == bookcase2.search_by_parameter("title4", "author4", "genre1") == bookcase3.search_by_parameter("title4", "author4", "genre1") == bookcase4.search_by_parameter("title4", "author4", "genre1") == [book4], "test failed search_by_parameter book4 after add_new_book"

  assert bookcase1.is_empty() == bookcase2.is_empty() == bookcase3.is_empty() == bookcase4.is_empty() == 0, "test failed is_empty after add_new_book"

  assert bookcase1.sum_pages("", "") == 1000, "test failed bookcase1 sum_pages after add_new_books"
  assert bookcase1.sum_pages("", "") == 800, "test failed bookcase2 sum_pages after add_new_books"
  assert bookcase1.sum_pages("", "") == 500, "test failed bookcase3 sum_pages after add_new_books"
  assert bookcase4.sum_pages("", "") == 400, "test failed bookcase4 sum_pages after add_new_books"

  assert bookcase1.order_by_parameter("pages") == [book4, book3, book2, book1], "test failed bookcase1 order_by_parameter after add_new_book"