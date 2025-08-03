from django.shortcuts import render
from relationship_app.models import Book 
from relationship_app.models import Library
from .models import Library  
from django.views.generic import DetailView 

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)  # Filter books by the library
        return context