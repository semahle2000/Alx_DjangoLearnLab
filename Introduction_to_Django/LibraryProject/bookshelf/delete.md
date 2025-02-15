# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()
# Output: (1, {'bookshelf.Book': 1})