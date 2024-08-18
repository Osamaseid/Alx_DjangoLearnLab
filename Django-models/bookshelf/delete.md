# Delete Operation

## Python Command
```python
from bookshelf.models import Book
# Deleting the book instance
book.delete()

# Verifying the deletion by trying to retrieve all books
books = Book.objects.all()
print(books)

## Expected Output
>>> books
<QuerySet []>
