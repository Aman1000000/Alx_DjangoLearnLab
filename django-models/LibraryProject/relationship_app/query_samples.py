import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Fetch the librarian associated with the library
        librarian = library.librarian  
        return librarian
    except Library.DoesNotExist:
        return None