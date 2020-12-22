from classes import Book
from classes import Bookcase
from datetime import date
import csv

def open_bookcase():
  try:
    with open('bookcase.csv', 'r') as bookcase_file:
      csv_reader = csv.reader(bookcase_file)
      next(csv_reader)
      books = []
      for line in csv_reader:
        books.append(Book(line[0], line[1], line[2], line[3], int(line[4])))

  except FileNotFoundError:
    with open('bookcase.csv', 'w') as bookcase_file:
      csv_writer = csv.writer(bookcase_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow(['title','author','genre','reading_date','pages'])
    books = []

  return Bookcase(books)

def new_book(bookcase):
  title = input("What is its title? ")
  author = input("Who is the author? ")
  genre = input("Which genre it is? ")
  pages = input("How many pages does it have? ")
  today_date = date.today()
  with open('bookcase.csv', 'a') as bookcase_file:
    csv_writer = csv.writer(bookcase_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([title, author, genre, str(today_date), pages])
  return Book(title, author, genre, date, int(pages))

def search(bookcase):
  parameter = input("Which is the paramater?(Title, Author, Genre, Pages, Reading_date) ")
  value = input("What are you looking for? ")
  result = Bookcase(list(bookcase.search_by_parameter(parameter, value)))
  if result.is_empty():
    print("Didn't find anything.")
  else:
    result.print()

def main():
  print("Welcome to your SmartBookcase! What would you want today?\n")

  bookcase = open_bookcase()

  while True:
    command = input("Type 1 if you want to add a new book to your bookcase.\nType 2 if you want to see all of your bookcase.\nType 3 if you want to search by something in your bookcase.\nType 4 if you want to know how much pages you have read.\nType 5 if you want to QUIT.\n")
    try:
      command = int(command)
    except:
      print("Please, type a valid command.")
      continue
    if command == 1:
      bookcase.add_new_book(new_book(bookcase))
    elif command == 2:
      bookcase.print()
    elif command == 3:
      search(bookcase)
    elif command == 4:
      print(bookcase.all_pages())
    elif command == 5:
      break;
    elif command != 0:
      print("Please, type a valid command.")
    

if __name__ == "__main__":
    main()
