from django.shortcuts import render
from relationship_app.models import Book, Library  # Import both models
from django.views.generic import DetailView 

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library  # Specify the model for this view
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # Name of the context variable to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Call the base implementation first
        context['books'] = Book.objects.filter(library=self.object)  # Fetch books related to the library
        return context

