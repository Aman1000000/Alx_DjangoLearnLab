from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView  
from .models import Library  
from relationship_app.models import Book  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
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
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')  # Redirect to a suitable page after login
    return render(request, 'relationship_app/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})