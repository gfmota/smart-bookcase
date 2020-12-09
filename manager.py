import os.path
import csv

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

def main():
  printf("Welcome to your SmartBookcase! What would you want today?\n")
  while True:
    command = input("Type 1 if you want to add a new book to your bookcase.\nType 2 if you want to see all of your bookcase.\nType 3 if you want to search by something in your bookcase.\nType 4 if you want to quit.")
    if command == 1:
      printf("You want to add a new book\n")
    elif command == 2:
      printf("You want to see all of your books\n")
    elif command == 3:
      printf("You want to search something in your bookcase\n")
    elif commad == 4:
      break;
    else:
      printf("Please, type a valid command.\n")


if __name__ == ‘__main__’:
    main()