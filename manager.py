from classes import Book
from classes import Bookcase
from datetime import date
import sqlite3

def new_book(cursor):
  title = input("What is its title? ").strip().lower()
  author = input("Who is the author? ").strip().lower()
  genre = input("Which genre it is?(Separate different genres with space)").strip()
  pages = int(input("How many pages does it have? ").strip())
  today_date = date.today()

  cursor.execute("INSERT INTO Bookcase VALUES (?, ?, ?, ?, ?)", (title, author, genre, str(today_date), pages))
  
  return Book(title, author, genre, today_date, pages)

def print_by_parameter(bookcase):
  while True:
    parameter = input("By which parameter would you like to order it? (title, author, pages or reading_date) ").strip()
    if parameter != "title" and parameter != "author" and parameter != "pages" and parameter != "reading_date":
      print("Please enter a valid parameter.")
      continue
    return bookcase.order_by_parameter(parameter)

def search(bookcase):
  title = input("What title you looking for? ")
  author = input("What author you looking for? ")
  genre = input("What genre you looking for? ")
  result = Bookcase(bookcase.search_by_parameter(title.strip(), author.strip(), genre.strip()))
  
  if result.is_empty():
    print("Didn't find anything.")
  else:
    result.print()

def sum_pages(bookcase):
  print("Please enter the dates in this form YYYY-MM-DD\nLeave in blank to count all bookcase's lifetime")
  date_from = input("Date from: ")
  date_to = input("Date to: ")
  return bookcase.sum_pages(date_from, date_to)

def main():
  print("Welcome to your SmartBookcase! What would you want today?\n")
  
  conn = sqlite3.connect('bookcase.sqlite')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS Bookcase (title TEXT, author TEXT, genre TEXT, reading_date TEXT, pages INTEGER)")
  bookcase = cursor.execute("SELECT * FROM Bookcase").fetchall()
  books = list()
  for book in bookcase:
    books.append(Book(book[0], book[1], book[2], date.fromisoformat(book[3]), int(book[4])))
  bookcase = Bookcase(books)

  while True:
    command = input("Type 1 if you want to add a new book to your bookcase.\nType 2 if you want to see all of your bookcase.\nType 3 if you want to search by something in your bookcase.\nType 4 if you want to know how much pages you have read.\nType 5 if you want to QUIT.\n")
    
    try:
      command = int(command)
    except:
      print("Please, type a valid command.")
      continue
    
    if command == 1:
      bookcase.add_new_book(new_book(cursor))
      conn.commit()
    elif command == 2:
      print_by_parameter(bookcase).print()
    elif command == 3:
      search(bookcase)
    elif command == 4:
      print(sum_pages(bookcase))
    elif command == 5:
      break
    elif command != 0:
      print("Please, type a valid command.")
    print("--------------------------------------")
    

if __name__ == "__main__":
    main()
