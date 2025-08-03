
from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    list_filter = ('author',)  
    search_fields = ('title', 'author')  
# Register Book model
admin.site.register(Book)