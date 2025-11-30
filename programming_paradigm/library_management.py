class Book:
    def __init__(self, title, author):
        self.title = title           # Public
        self.author = author         # Public
        self._is_checked_out = False # Private

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book (make it available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of books

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print all available books in 'Title by Author' format."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
