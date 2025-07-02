import tkinter as tk
from tkinter import ttk

class LandingView:
    def __init__(self, root, on_view_books, on_add_book, message=None, message_color=None):
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        if message:
            color = message_color if message_color else "green"
            msg_label = tk.Label(self.frame, text=message, fg=color, font=("Helvetica", 10))
            msg_label.pack(pady=(10, 5))

        label = tk.Label(self.frame, text="Welcome to Small Library", font=("Helvetica", 16))
        label.pack(pady=10)

        view_button = tk.Button(self.frame, text="View Books", command=on_view_books)
        view_button.pack(pady=5)

        add_button = tk.Button(self.frame, text="Add New Book", command=on_add_book)
        add_button.pack(pady=5)

    def destroy(self):
        self.frame.destroy()

class DataView:
    def __init__(self, root, books, on_back):
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        back_button = tk.Button(self.frame, text="Back", command=on_back)
        back_button.pack(pady=5)

        self.tree = ttk.Treeview(self.frame, columns=("Title", "Author", "ISBN", "Year"), show="headings")
        for col in ("Title", "Author", "ISBN", "Year"):
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True)
        self.tree.pack(fill=tk.BOTH, expand=True)

        for book in books:
            self.tree.insert("", tk.END, values=(book.title, book.author, book.isbn, book.published_year))

    def destroy(self):
        self.frame.destroy()


class AddBookView:
    def __init__(self, root, on_submit, on_cancel):
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.entries = {}
        for label_text in ("Title", "Author", "ISBN", "Year"):
            label = tk.Label(self.frame, text=label_text)
            label.pack()
            entry = tk.Entry(self.frame)
            entry.pack()
            self.entries[label_text.lower()] = entry

        submit = tk.Button(self.frame, text="Submit", command=self._submit)
        submit.pack(pady=10)

        cancel = tk.Button(self.frame, text="Cancel", command=on_cancel)
        cancel.pack()

        self.on_submit = on_submit

    def _submit(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        self.on_submit(data)

    def destroy(self):
        self.frame.destroy()
