import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Created: {book}")

# Retrieve the Book instance
book = Book.objects.get(title="1984")
print(f"Retrieved: {book.title}, {book.author}, {book.publication_year}")

# Update the Book title
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated: {book.title}")

# Delete the Book instance
book.delete()
print("Deleted the book instance")