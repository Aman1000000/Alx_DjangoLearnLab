# Delete

Import the Book model to use it:

```python
from bookshelf.models import Book

# Delete duplicates
books = Book.objects.filter(title="1984")
for book in books[1:]:  # Skip the first one
    book.delete()