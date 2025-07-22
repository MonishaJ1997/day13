from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

# Abstract Member
class Member(ABC):
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []

    @abstractmethod
    def role(self):
        pass

    def borrow_book(self, book, days=14):
        if book.available:
            book.available = False
            due = datetime.now() + timedelta(days=days)
            self._borrowed_books.append((book, due))
            print(f"{self._name} borrowed {book.title}, due on {due.date()}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, isbn):
        for i, (book, _) in enumerate(self._borrowed_books):
            if book.isbn == isbn:
                book.available = True
                self._borrowed_books.pop(i)
                print(f"{self._name} returned {book.title}")
                return
        print("Book not found in borrowed list.")

    def get_borrowed_books(self):
        return [(b.title, d.date()) for b, d in self._borrowed_books]

    def __str__(self):
        return f"Member: {self._name} (ID: {self._member_id})"

# Student as concrete Member
class Student(Member):
    def role(self):
        return "Student"

# Librarian with extra power to manage books
class Librarian(Member):
    def role(self):
        return "Librarian"

# Library Class
class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"Book '{book.title}' added.")

    def remove_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                self.__books.remove(book)
                print(f"Book '{book.title}' removed.")
                return
        print("Book not found.")

    def search_books(self, keyword):
        results = [book for book in self.__books if keyword.lower() in book.title.lower()]
        for book in results:
            print(book)
        if not results:
            print("No matching books found.")

    def register_member(self, member):
        self.__members.append(member)
        print(f"{member} registered.")

    def __len__(self):
        return len(self.__books)

    def __str__(self):
        return f"Library with {len(self)} books and {len(self.__members)} members."

# Transaction Tracker
class Transaction:
    def __init__(self):
        self.records = []

    def log(self, member, book, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.records.append(f"{timestamp} - {member._Member__name} {action} '{book.title}'")

    def history(self):
        for rec in self.records:
            print(rec)



# Setup
lib = Library()
lib.add_book(Book("Python Basics", "John Doe", "111"))
lib.add_book(Book("OOP in Python", "Alice", "222"))

student = Student("Ram", "S101")
librarian = Librarian("Ms. Priya", "L201")

lib.register_member(student)
lib.register_member(librarian)

print(lib)

# Actions
lib.search_books("Python")
student.borrow_book(lib._Library__books[0])
print(student.get_borrowed_books())
student.return_book("111")
