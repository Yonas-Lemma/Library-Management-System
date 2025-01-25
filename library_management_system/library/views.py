from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from datetime import datetime

# Create your views here.


def home(request):
   books=Book.objects.all()
   return render(request, 'book_list.html',{'books':books})
def addbook(request):
   if request.method == 'POST':
      title=request.POST['title']
      author=request.POST['author']
      image_address=request.POST['image_address']
      isbn=request.POST['isbn']
      date=request.POST['date']
      Copies_available=request.POST['Copies_available']



      published_date = datetime.strptime(date, '%Y-%m-%d').date()


      new_book=Book(title=title, author=author, image_address=image_address, isbn=isbn,  published_Date=published_date, Copies_available=Copies_available)
      new_book.save()
      

   
   return render(request,'addbook.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        image_address=request.POST['image_address']
        book.isbn = request.POST['isbn']
        book.published_Date = request.POST['date']
        book.Copies_available = request.POST['Copies_available']
        book.image_address = request.POST['image_address']
        book.save()
        return redirect('home')

    return render(request, 'edit_book.html', {'book': book})

def delete(request,id):
   book=Book.objects.get(id=id)
   book.delete()
   return redirect('home')

def book_view(request):
   books=Book.objects.all()
   return render(request,'test.html',{'books':books})

