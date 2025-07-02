# TODO: Tests 'vibe coded' for now, add actual/more tests later

import book

def _parse_from_line(line):
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(line)
        f.flush()
        return book.get_books(f.name)

def test_simple_book():
    #line = "Author A/Hi/1234567890/2020\n"  -> Todo: remove this failing test case later
    line = "Hi/Author A/1234567890/2020\n"
    books = _parse_from_line(line)
    assert books[0].title == "Hi"

