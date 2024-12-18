# Library Management System

## Overview
This project is a **Library Management System** built using Python and the Tkinter library. It allows users to manage a collection of books, including adding, editing, deleting, searching, and saving book records to a CSV file.

## Features
1. **Add Books**: Add new books to the library.
2. **Edit Books**: Update details of existing books.
3. **Delete Books**: Remove books from the library.
4. **Search Books**: Search for books by title or author.
5. **Save Library**: Save the library records to a CSV file.
6. **Restore Library**: Load library records from a CSV file.

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- `csv` module (built-in with Python)
- `os` module (built-in with Python)

## File Structure
- `LibraryApp`: The main class handling the application logic.
- `Book`: A class representing a book entity.
- `Library.csv`: A file used to store the library records.

## Setup Instructions
1. Make sure you have Python 3 installed.
2. Save the script to a file (e.g., `library_management.py`).
3. Run the script using the following command:
   ```bash
   python library_management.py
   ```

## Usage

### Add a Book
1. Click on the **Add Book** button.
2. Enter the book details (Title, Author, Copies) in the popup window.
3. Click the **Add** button to save the book.

### Edit a Book
1. Select a book from the table.
2. Click on the **Edit Book** button.
3. Update the book details in the popup window.
4. Click the **Update** button to save the changes.

### Delete a Book
1. Select a book from the table.
2. Click on the **Delete Book** button.
3. Confirm the deletion in the popup dialog.

### Search for a Book
1. Enter a search term (title or author) in the search bar.
2. Click the **Search** button to filter the results.
3. To clear the search, click the **Clear Search** button.

### Save the Library
- Click on the **Save Library** button to save the library to the `Library.csv` file.

### Restore Library
- Click on the **Show Library** button to reload records from the `Library.csv` file.

## Code Structure

### Classes
#### 1. `Book`
- Represents a book with the following attributes:
  - `title` (str): Title of the book.
  - `author` (str): Author of the book.
  - `copies` (int): Number of copies available.

#### 2. `LibraryApp`
- Inherits from `Book` and handles the application logic.

### Key Functions
1. **`add_book()`**: Adds a new book to the library and saves it to the CSV file.
2. **`edit_book()`**: Edits the details of a selected book.
3. **`delete_book()`**: Deletes a selected book and updates the CSV file.
4. **`search_book()`**: Searches for books matching a query.
5. **`clear_search()`**: Clears the search and restores all books.
6. **`save_library()`**: Saves the library to a CSV file.
7. **`restore_library()`**: Loads books from the CSV file.

### CSV Operations
- **`save_book_to_csv()`**: Appends a new book to `Library.csv`.
- **`update_library_csv()`**: Updates the `Library.csv` file with the current library state.

## Example CSV Format
```csv
Title,Author,Copies
The Great Gatsby,F. Scott Fitzgerald,5
To Kill a Mockingbird,Harper Lee,3
1984,George Orwell,4
```

## Acknowledgments
- **Tkinter**: For providing the GUI functionality.
- **CSV Module**: For managing book data storage.
- **OS Module**: For file operations.

