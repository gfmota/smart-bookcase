import classes
import os.path
import csv

def main():
  print("Welcome to your SmartBookcase! What would you want today?\n")
  while True:
    command = input("Type 1 if you want to add a new book to your bookcase.\nType 2 if you want to see all of your bookcase.\nType 3 if you want to search by something in your bookcase.\nType 4 if you want to quit.")
    if command == 0:
      print("You want to view again\n")
    elif command == 1:
      print("You want to add a new book\n")
    elif command == 2:
      print("You want to see all of your books\n")
    elif command == 3:
      print("You want to search something in your bookcase\n")
    elif commad == 4:
      break;
    else:
      print("Please, type a valid command.\n")


if __name__ == "__main__":
    main()
