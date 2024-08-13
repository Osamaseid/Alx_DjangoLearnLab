### Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check if the book is deleted
books = Book.objects.all()
print(books)
```
