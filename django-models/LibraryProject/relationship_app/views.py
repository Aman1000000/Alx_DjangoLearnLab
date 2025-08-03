from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Library  
from relationship_app.models import Book  

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library  # Specify the model for this view
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['books'] = Book.objects.filter(library=self.object)  
        return context