import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        books_by_author = Book.objects.filter(author__name=author_name)
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"Author named {author_name} does not exist.")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"Library named {library_name} does not exist.")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"Librarian of {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian for library named {library_name} does not exist.")

# Example usage
if __name__ == "__main__":
    # Replace with actual names from your database
    get_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
