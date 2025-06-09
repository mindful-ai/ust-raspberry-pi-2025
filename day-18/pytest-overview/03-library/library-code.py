# library.py

class BookNotAvailableError(Exception):
    pass

class InvalidReturnError(Exception):
    pass

class Library:
    def __init__(self, books):
        self.available_books = set(books)
        self.borrowed_books = set()

    def borrow_book(self, title):
        if title not in self.available_books:
            raise BookNotAvailableError(f"'{title}' is not available.")
        self.available_books.remove(title)
        self.borrowed_books.add(title)

    def return_book(self, title):
        if title not in self.borrowed_books:
            raise InvalidReturnError(f"'{title}' was not borrowed.")
        self.borrowed_books.remove(title)
        self.available_books.add(title)
