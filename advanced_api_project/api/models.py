from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

# The Author model represents book authors, storing their names.
# Each author can have multiple books, modeled using a ForeignKey in the Book model.

# The Book model stores the title and publication year of each book.
# It has a ForeignKey to Author, establishing a one-to-many relationship from Author to Books.

