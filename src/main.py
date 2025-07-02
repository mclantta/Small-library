import sys
import os
import tkinter as tk
from controller import DataController

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        open(file_path, 'w').close()  # Create empty file

    root = tk.Tk()
    root.title('Small Library Program')
    root.geometry("800x300")
    DataController(file_path, root)
    root.mainloop()

if __name__ == "__main__":
    main()

