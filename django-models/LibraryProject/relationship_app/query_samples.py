import os
import django

# Set up the Django environment
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
        # Retrieve the librarian using the library instance
        librarian = Librarian.objects.get(library=library)  # Modify this line
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None  # Handle case where no librarian exists for the library

if __name__ == "__main__":
    library_name = "Your Library Name"  # Replace with your library's name
    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
    else:
        print(f"No librarian found for {library_name}.")