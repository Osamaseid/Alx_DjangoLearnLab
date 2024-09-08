from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']



# BookSerializer serializes the title, publication year, and author field
# It includes custom validation to ensure the publication year is not in the future.
# AuthorSerializer serializes the author's name and includes a nested BookSerializer
# to serialize related books, using the 'books' related_name defined in the Book model.

