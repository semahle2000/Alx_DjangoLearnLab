# CRUD Operations

## Create
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output: <Book: 1984>
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Output: <Book: Nineteen Eighty-Four>
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output: (1, {'bookshelf.Book': 1})