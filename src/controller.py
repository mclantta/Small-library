from book import get_books

class DataController:
    def __init__(self, file_path, view):
        self.file_path = file_path
        self.view = view
        self.load_data()

    def load_data(self):
        books = get_books(self.file_path)
        self.view.display_books(books)
