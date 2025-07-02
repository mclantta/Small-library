from book import get_books, Book, add_book
from view import LandingView, LibraryContentsView, AddBookView
from tkinter import messagebox

class DataController:
    def __init__(self, file_path, root):
        self.root = root
        self.file_path = file_path
        self.current_view = None
        self.show_landing()

    def clear_view(self):
        if self.current_view:
            self.current_view.destroy()

    def show_landing(self, message=None, message_color=None):
        self.clear_view()
        self.current_view = LandingView(self.root, self.show_books, self.show_add_book, message, message_color)

    def show_books(self):
        self.clear_view()
        books = get_books(self.file_path)
        self.current_view = LibraryContentsView(self.root, books, self.show_landing)

    def show_add_book(self):
        self.clear_view()
        self.current_view = AddBookView(self.root, self.submit_book, self.show_landing)

    def submit_book(self, data):
        if all(data.values()):
            new_book = Book(data["title"], data["author"], data["isbn"], data["year"])

            confirm = messagebox.askyesno(
                "Confirm Add",
                f"You are adding the following book:\n\n"
                f"Title: {new_book.title}\n"
                f"Author: {new_book.author}\n"
                f"ISBN: {new_book.isbn}\n"
                f"Year: {new_book.published_year}\n\n"
                "Do you want to continue?"
            )

            if confirm:
                add_book(self.file_path, new_book)
                msg = f"Library updated. Book added with this info: {new_book.title}, {new_book.author}, {new_book.isbn}, {new_book.published_year}"
                self.show_landing(msg, "green")
            else:
                self.show_landing("Book addition cancelled by user.", "red")

        else:
            self.show_landing("Book not added. Please fill all fields.", "red")
