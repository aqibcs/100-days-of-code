class Library:
    def __init__(self) -> None:
        self.no_of_books = 0
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
    
    def get_no_of_books(self):
        return self.no_of_books

    def print_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)


# Create a library instance
my_library = Library()

# Add books to the library
my_library.add_book("The Catcher in the Rye by J.D. Salinger")
my_library.add_book("To Kill a Mockingbird by Harper Lee")
my_library.add_book("1984 by George Orwell")

# Print all books in the library
print("Books in the library")
my_library.print_books()

# Get the number of books in the library
print("\nNumber of books in the library:", my_library.get_no_of_books())

# Demonstrate that the data does not persist after program termination
print("\nThis program does not persist the library's data after it is stopped.")