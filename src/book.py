class Book:
    def __init__(self, title: str, author: str, isbn: str, published_year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_year = published_year

def get_books(file_path):
    books = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split('/')
            if len(parts) == 4:
                books.append(Book(*parts))
    
    # Sort by publishing year
    books.sort(key=lambda b: b.published_year)
    return books

def add_book(file_path, book):
    with open(file_path, 'a+') as f:
        f.seek(0)
        if f.read().endswith('\n') or f.tell() == 0:
            f.write(f"{book.title}/{book.author}/{book.isbn}/{book.published_year}\n")
        else:
            f.write(f"\n{book.title}/{book.author}/{book.isbn}/{book.published_year}\n")
