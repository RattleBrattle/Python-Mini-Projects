"""
* Author: Basel Mohamed Mostafa Sayed
* Email: baselmohamed802@gmail.com
* Description: This file contains all the classes and functions for the Library program.
"""

class Book:
    """Class Constructor"""
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True
        self.isBorrowed = False

    """ Function to toggle Availability"""
    def toggle_availability(self) -> None:
        self.isAvailable = not self.isAvailable

    """ Function to toggle if book is borrowed or not"""
    def toggle_borrowed(self) -> None:
        self.isBorrowed = not self.isBorrowed

    """ Function to print Availability"""
    def print_availability(self) -> None:
        if self.isAvailable:
            print(f"The book '{self.title}' is Available.")
        elif not self.isAvailable and self.isBorrowed:
            print(f"The book '{self.title}' is currently borrowed, sorry.")
        else:
            print(f"The book '{self.title}' is Not Available currently.")

    """Function to print all info related to the book"""
    def print_book_info(self) -> None:
        print(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Available: {self.isAvailable}\n"
            f"Borrowed: {self.isBorrowed}"
        )

class Library:  # Changed from 'library' to 'Library'
    """Class Constructor"""
    def __init__(self):
        self.books: list[Book] = []

    """Function to add a book to the library"""
    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"The Book titled: '{book.title}', Has been added successfully!")

    """Function to search for a specific book using title"""
    def find_book_by_title(self, title: str) -> Book | None:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

    """Function to display all books in Library"""
    def display_all_books(self) -> None:
        if not self.books:
            print("There are no books in Library yet")
            return
        else:
            for book in self.books:
                book.print_book_info()
                print("-" * 40)

    """Function to Borrow and mark a book as borrowed"""
    def borrow_book(self, title: str) -> None:
        book = self.find_book_by_title(title)
        if book:
            if book.isAvailable:
                book.toggle_availability()
                book.toggle_borrowed()
                print(f"Book titled '{book.title}' has been borrowed successfully!")
            else:
                print(f"Sorry but book '{book.title}' is already borrowed or not available.")

    """Function to return a borrowed book"""
    def return_book(self, title: str) -> None:
        book = self.find_book_by_title(title)
        if book:
            if not book.isAvailable:
                book.toggle_availability()
                book.toggle_borrowed()
                print(f"Book titled '{book.title}' has been returned successfully!")
            else:
                print(f"Sorry but book '{book.title}' is already available.")

"""Function to add a book to the Library"""
def add_book_lib(lib: Library) -> None:
    print("\nAdding a new book:")
    
    # Get validated title
    book_title = validate_book_title(lib)
    if book_title is None:  # In case validation fails
        return
    
    # Get other details
    book_author = input("Author: ").strip()
    if not book_author:
        print("Author cannot be empty!")
        return
        
    book_isbn = validate_isbn_lib()
    if book_isbn is None:
        return

    # Create and add new book
    new_book = Book(title=book_title, author=book_author, isbn=book_isbn)
    lib.add_book(new_book)

"""Function to display all books in Library"""
def show_all_books_lib(lib: Library) -> None:
    lib.display_all_books()

"""Function to borrow a book"""
def borrow_book_lib(lib: Library) -> None:
    book_title = str(input("Enter the title of the book you want to borrow: "))
    lib.borrow_book(book_title)

"""Function to return a book"""
def return_book_lib(lib: Library) -> None:
    book_title = str(input("Enter the title of the book you want to return: ")) 
    lib.return_book(book_title)

"""Function to find a specific book in the library"""
def specific_book_lib(lib: Library) -> None:
    book_title = str(input("Enter the title of the book you want to find: "))
    
    book = lib.find_book_by_title(book_title)
    if book:
        book.print_book_info()  
    else:
        print(f"Book '{book_title}' was not found.")

"""Simple function to validate ISBN number"""
def validate_isbn_lib() -> str:
    correct_input = False

    while not correct_input:
        book_isbn_temp = str(input("ISBN: "))

        # Checking if the ISBN is between correct range or not
        if len(book_isbn_temp) >= 10 and len(book_isbn_temp) <= 13:
            correct_input = True
            return book_isbn_temp
        else:
            correct_input = False
            print("The entered ISBN is invalid, valid range is from 10 to 13 numbers....")

"""Function to check for duplicate book titles"""
def validate_book_title(lib: Library) -> str:
    while True:
        book_title_temp = input("Book title: ").strip()
        if not book_title_temp:
            print("Title cannot be empty!")
            continue
        
        # Check if book already exists
        existing_book = lib.find_book_by_title(book_title_temp)
        if existing_book is None:  # Only return if book doesn't exist
            return book_title_temp
        print("Error: A book with this title already exists!")