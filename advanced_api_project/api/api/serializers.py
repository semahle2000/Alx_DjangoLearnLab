from rest_framework import serializers
from .models import Author, Book

'''
BoookSerializer handles serialization of the Book model and validates publication_year.
AuthorSerializer serializes the Author model and includes nested BookSerializer for related books
'''
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'
        
    def validate_publication_year(self, value):
        from datetime import date
        current_year=date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSeriakizer):
    book = BookSerializer(many-True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name','books']