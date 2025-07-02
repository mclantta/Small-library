import tkinter as tk
from tkinter import ttk

class DataView:
    def __init__(self, root):
        self.root = root
        self.root.title("Small Library")

        self.tree = ttk.Treeview(root, columns=("Title", "Author", "ISBN", "Year"), show="headings")
        for col in ("Title", "Author", "ISBN", "Year"):
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def display_books(self, books):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in books:
            self.tree.insert("", tk.END, values=book.as_tuple())
