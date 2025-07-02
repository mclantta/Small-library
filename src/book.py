class Book:

    # Sama juttu täällä, miksi nuo "author" etc. toistuu niin monesti??
    # Eikö ne pitäis olla vain 1 paikkaa, jotta helppo muuttaa kun muutoksia tulee

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
    
    # Sort by publishing year (convert to int for correct sort)
    books.sort(key=lambda b: int(b.published_year))   # HUOM, jos vaihdat tyyppiä, nii sit tätä int converttausta mikä on nyt, ei tarvisikaan tehdä
    return books

def add_book(file_path, book):
    with open(file_path, 'a+') as f:
        f.seek(0)
        if f.read().endswith('\n') or f.tell() == 0:
            f.write(f"{book.title}/{book.author}/{book.isbn}/{book.published_year}\n")
        else:
            f.write(f"\n{book.title}/{book.author}/{book.isbn}/{book.published_year}\n")
