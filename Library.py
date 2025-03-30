import json
import os

class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

class LibraryManager:
    def __init__(self):
        self.library = []
        self.load_library()

    def add_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = int(input("Enter publication year: "))
            genre = input("Enter genre: ")
            read = input("Have you read it? (y/n): ").lower() == 'y'
            
            book = Book(title, author, year, genre, read)
            self.library.append(book)
            print(f"\n'{title}' has been added to the library!")
        except ValueError:
            print("Invalid input! Year must be a number.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        initial_length = len(self.library)
        self.library = [book for book in self.library if book.title.lower() != title.lower()]
        
        if len(self.library) < initial_length:
            print(f"\n'{title}' has been removed from the library!")
        else:
            print("\nBook not found!")

    def search_book(self):
        search_term = input("Enter title or author to search: ").lower()
        matches = [book for book in self.library 
                  if search_term in book.title.lower() or search_term in book.author.lower()]
        
        if matches:
            print("\nMatching books:")
            self.display_books(matches)
        else:
            print("\nNo matching books found!")

    def display_books(self, books=None):
        if books is None:
            books = self.library
        
        if not books:
            print("\nLibrary is empty!")
            return
        
        print("\nLibrary Contents:")
        print("-" * 50)
        for i, book in enumerate(books, 1):
            read_status = "Read" if book.read_status else "Unread"
            print(f"{i}. {book.title}")
            print(f"   Author: {book.author}")
            print(f"   Year: {book.year}")
            print(f"   Genre: {book.genre}")
            print(f"   Status: {read_status}")
            print("-" * 50)

    def display_stats(self):
        total_books = len(self.library)
        if total_books == 0:
            print("\nLibrary is empty!")
            return
        
        read_books = len([book for book in self.library if book.read_status])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        
        print("\nLibrary Statistics:")
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {percentage_read:.1f}%")

    def save_library(self):
        library_data = [{
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'genre': book.genre,
            'read_status': book.read_status
        } for book in self.library]
        
        with open('library.txt', 'w') as f:
            json.dump(library_data, f)
        print("\nLibrary saved to file!")

    def load_library(self):
        if os.path.exists('library.txt'):
            with open('library.txt', 'r') as f:
                try:
                    library_data = json.load(f)
                    self.library = [Book(book['title'], book['author'], 
                                      book['year'], book['genre'], 
                                      book['read_status']) 
                                  for book in library_data]
                    print("Library loaded from file!")
                except json.JSONDecodeError:
                    print("Error loading library file. Starting with empty library.")

def main():
    manager = LibraryManager()
    menu = {
        '1': ('Add a book', manager.add_book),
        '2': ('Remove a book', manager.remove_book),
        '3': ('Search for a book', manager.search_book),
        '4': ('Display all books', lambda: manager.display_books()),
        '5': ('Display statistics', manager.display_stats),
        '6': ('Exit', None)
    }

    while True:
        print("\n=== Personal Library Manager ===")
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice in menu:
            if choice == '6':
                manager.save_library()
                print("Goodbye!")
                break
            menu[choice][1]()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()