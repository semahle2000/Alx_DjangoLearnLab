from rest_framework import serializers
from .models import Book
from .models import Author

"""
The BookSerializer serializes all fields of the Book model and includes custom validation for the publication year.
The AuthorSerializer serializes the name field and includes a nested BookSerializer to serialize related books.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']