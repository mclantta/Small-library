import sys
import os
import tkinter as tk

from book import Book
from view import DataView
from controller import DataController

def main():
    new_book = Book("Vuosi herrasmiehenä", "Joonas Konstig", "978-951-0-42229-8", 2017)
    print(new_book.author)

    if len(sys.argv) < 2:
        print("Usage: python src/main.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found.")
        sys.exit(1)

    root = tk.Tk()
    view = DataView(root)
    controller = DataController(file_path, view)
    root.mainloop()

if __name__ == "__main__":
    main()
