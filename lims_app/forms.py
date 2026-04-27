from django import forms
from .models import Book, Collection

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'available_copies', 'publication_date', 'isbn']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'book', 'date_borrowed', 'due_date', 'status']