class Book:

    def __init__(self, title: str, author: str, isbn: str, publishing_year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publishing_year = publishing_year

    def as_tuple(self):
        return (self.author, self.title, self.isbn, self.publishing_year)

def get_books(file_path):
    books = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split('/')
            if len(parts) == 4:
                author, title, isbn, publishing_year = parts
                books.append(Book(author, title, isbn, publishing_year))
    return books
