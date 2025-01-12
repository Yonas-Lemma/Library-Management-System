from django import form
from .models import Book
class EditBook(form.Form):
    class meta:
        model=Book
        filds=['title', 'author', 'isbn', 'published_Date', 'Copies_available']