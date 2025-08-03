from django.shortcuts import render
from relationship_app.models import Book
from django.views import DetailView
from relationship_app.models import Library

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})  # Render the template with the book list

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  
    context_object_name = 'library'