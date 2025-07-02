"""
* Author: Basel Mohamed Mostafa Sayed
* Email: baselmohamed802@gmail.com
* Description: This file is the main code for the library program.
"""
from Library import (
    Library,  # Matches the class name
    add_book_lib,
    borrow_book_lib,
    return_book_lib,
    show_all_books_lib,
    specific_book_lib
)

lib = Library()
user_quit = False

# Main program loop
while not user_quit:
    correct_input = False
    print("\nWelcome to the Library program!")
    print("=" * 40)
    print("Which operation do you want to perform:\n" 
          "1) Add a Book.\n"
          "2) Display All Books currently available stored in Library.\n"
          "3) Borrow a book.\n"
          "4) Return a book.\n"
          "5) Search for a book by title.\n"
          "6) Exit.")

    while not correct_input:
        try:
            user_input = int(input("Input (1-6): "))
            if 1 <= user_input <= 6:
                correct_input = True
            else:
                print("Invalid input, please enter a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    match user_input:
        case 1:
            add_book_lib(lib)
        case 2:
            show_all_books_lib(lib)
        case 3:
            borrow_book_lib(lib)
        case 4:
            return_book_lib(lib)
        case 5:
            specific_book_lib(lib)
        case 6:
            print("Exiting application.....")
            user_quit = True