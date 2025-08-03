1. Open `bookshelf/admin.py`.
2. Import the `Book` model:
   ```python
   from .models import Book
   admin.site.register(Book)