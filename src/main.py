from book import Book

def main():
    new_book = Book("Vuosi herrasmiehenä", "Joonas Konstig", "978-951-0-42229-8", 2017)
    print(new_book)
    print(new_book.author)

if __name__=="__main__":
    main()
