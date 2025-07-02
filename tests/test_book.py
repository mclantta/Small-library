import os
import tempfile
import pytest
from book import Book, get_books, add_book

# ---- Fixture for a temporary file ----
@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp()
    yield path
    os.close(fd)
    os.remove(path)

# ---- Parameterized tests for get_books ----
@pytest.mark.parametrize("line, expected_count, expected_title", [
    ("Book One/Author One/1234567890/2000\n", 1, "Book One"),
    ("Incomplete Line Without Enough Fields\n", 0, None),
    ("1984/Author X/1111111111/1949\n", 1, "1984"),
    ("A Very Long Book Title That Keeps Going On And On/Long Author/9999999999/2021\n", 1, "A Very Long Book Title That Keeps Going On And On")
])
def test_get_books_various_cases(temp_file, line, expected_count, expected_title):
    with open(temp_file, 'w') as f:
        f.write(line)
    books = get_books(temp_file)
    assert len(books) == expected_count, f"Expected {expected_count} book, but got {len(books)}. Input was: {line.strip()}"
    if expected_title:
        assert books[0].title == expected_title, f"Expected title '{expected_title}' but got '{books[0].title}'"

# ---- Test for add_book ----
def test_add_book_writes_properly(temp_file):
    book = Book("Test Author", "Test Title", "123456", "2024")
    add_book(temp_file, book)
    with open(temp_file, 'r') as f:
        content = f.read().strip()
    assert content == "Test Author/Test Title/123456/2024"
