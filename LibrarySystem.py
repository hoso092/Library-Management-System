import os
import tkinter as tk
import csv
from tkinter import messagebox, ttk


class Book:
    def __init__(self, title="", author="", copies=0):
        self.title = title
        self.author = author
        self.copies = copies


class LibraryApp(Book):
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1000x800")
        self.library = []
        super().__init__(title="", author="", copies=0)

        # Window Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3"
        )
        style.map('Treeview', background=[('selected', '#34A2FE')])

        # Search Frame
        search_frame = tk.Frame(root, bg="#f0f0f0")
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(search_frame, text="Search Book:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_book, bg="#34A2FE", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Clear Search", command=self.clear_search, bg="#FF7F50", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

        # Treeview (Table)
        self.tree = ttk.Treeview(root, columns=("Title", "Author", "Copies"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Copies", text="Copies")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Button Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text="Add Book", command=self.add_book, bg="#32CD32", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Book", command=self.edit_book, bg="#1E90FF", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Book", command=self.delete_book, bg="#DC143C", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Save Library", command=self.save_library, bg="#808080", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Library", command=self.restore_library, bg="#FF8C00", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

    def add_book(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Book")
        popup.geometry("300x600")

        tk.Label(popup, text="Title:", font=("Arial", 12)).pack(pady=5)
        title_entry = tk.Entry(popup, font=("Arial", 12))
        title_entry.pack(pady=5)

        tk.Label(popup, text="Author:", font=("Arial", 12)).pack(pady=5)
        author_entry = tk.Entry(popup, font=("Arial", 12))
        author_entry.pack(pady=5)

        tk.Label(popup, text="Copies:", font=("Arial", 12)).pack(pady=5)
        copies_entry = tk.Entry(popup, font=("Arial", 12))
        copies_entry.pack(pady=5)

        def save_book():
            title = title_entry.get().strip()
            author = author_entry.get().strip()
            copies = copies_entry.get().strip()

            if not title or not author or not copies:
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                copies = int(copies)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for copies!")
                return

            book = Book(title, author, copies)
            self.library.append(book)
            self.tree.insert("", tk.END, values=(title, author, copies))
            self.save_book_to_csv(book)
            popup.destroy()

        tk.Button(popup, text="Add", command=save_book, bg="#32CD32", fg="white", font=("Arial", 12)).pack(pady=10)

    def save_book_to_csv(self, book):
        file_exists = os.path.exists('Library.csv')
        with open('Library.csv', 'a', newline='') as csvfile:
            fieldnames = ['Title', 'Author', 'Copies']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists or os.stat('Library.csv').st_size == 0:
                writer.writeheader()
            writer.writerow({'Title': book.title, 'Author': book.author, 'Copies': book.copies})
        messagebox.showinfo("Info", "Book saved to Library.csv!")

    def restore_library(self):
        if not os.path.exists('Library.csv') or os.stat('Library.csv').st_size == 0:
            messagebox.showinfo("Info", "No library data found.")
            return

        with open('Library.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            self.library.clear()
            self.tree.delete(*self.tree.get_children())
            for row in csvreader:
                title = row['Title']
                author = row['Author']
                copies = int(row['Copies'])
                self.library.append(Book(title, author, copies))
                self.tree.insert("", tk.END, values=(title, author, copies))

    def delete_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to delete.")
            return

        item = self.tree.item(selected_item)
        title = item["values"][0]

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{title}'?")
        if confirm:
            self.library = [book for book in self.library if book.title != title]
            self.tree.delete(selected_item)
            self.update_library_csv()

    def update_library_csv(self):
        with open('Library.csv', 'w', newline='') as csvfile:
            fieldnames = ['Title', 'Author', 'Copies']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.library:
                writer.writerow({'Title': book.title, 'Author': book.author, 'Copies': book.copies})
        messagebox.showinfo("Info", "Library updated!")

    def edit_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to edit.")
            return

        item = self.tree.item(selected_item)
        title = item["values"][0]
        author = item["values"][1]
        copies = item["values"][2]

        popup = tk.Toplevel(self.root)
        popup.title("Edit Book")
        popup.geometry("300x600")

        tk.Label(popup, text="Title:", font=("Arial", 12)).pack(pady=5)
        title_entry = tk.Entry(popup, font=("Arial", 12))
        title_entry.insert(0, title)
        title_entry.pack(pady=5)

        tk.Label(popup, text="Author:", font=("Arial", 12)).pack(pady=5)
        author_entry = tk.Entry(popup, font=("Arial", 12))
        author_entry.insert(0, author)
        author_entry.pack(pady=5)

        tk.Label(popup, text="Copies:", font=("Arial", 12)).pack(pady=5)
        copies_entry = tk.Entry(popup, font=("Arial", 12))
        copies_entry.insert(0, copies)
        copies_entry.pack(pady=5)

        def save_edited_book():
            new_title = title_entry.get().strip()
            new_author = author_entry.get().strip()
            new_copies = copies_entry.get().strip()

            if not new_title or not new_author or not new_copies:
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                new_copies = int(new_copies)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for copies!")
                return

            self.tree.item(selected_item, values=(new_title, new_author, new_copies))
            for book in self.library:
                if book.title == title:
                    book.title = new_title
                    book.author = new_author
                    book.copies = new_copies
            self.update_library_csv()
            popup.destroy()

        tk.Button(popup, text="Update", command=save_edited_book, bg="#1E90FF", fg="white", font=("Arial", 12)).pack(pady=10)

    def search_book(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showerror("Error", "Please enter a search term.")
            return

        self.tree.delete(*self.tree.get_children())
        for book in self.library:
            if query in book.title.lower() or query in book.author.lower():
                self.tree.insert("", tk.END, values=(book.title, book.author, book.copies))

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        for book in self.library:
            self.tree.insert("", tk.END, values=(book.title, book.author, book.copies))

    def save_library(self):
        self.update_library_csv()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
