from zoneinfo import available_timezones

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Reader
from .forms import BookForm, CollectionForm
from django.shortcuts import get_object_or_404, redirect
from .models import Borrowing

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def readers(request):
    readers = Reader.objects.all()
    return render(request, "readers.html", {
        "current_tab": "readers",
        "readers": readers
    })

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST.get('student_name', '')
    return render(request, "welcome.html", context={'student_name': student_name})

def readers_tab(request):
    if request.method == 'POST':
        reader_name = request.POST.get('reader_name')
        reader_contact = request.POST.get('reader_contact')
        reference_id = request.POST.get('reference_id')  # ✅ FIXED

        Reader.objects.create(
            reader_name=reader_name,
            reader_contact=reader_contact,
            reference_id=reference_id,
            reader_address=request.POST.get('reader_address', '')
        )

        return redirect('readers_tab')

    query = request.GET.get('query', '')
    if query:
        readers = Reader.objects.filter(reader_name__icontains=query)
    else:
        readers = Reader.objects.all()

    return render(request, "readers.html", {
        "current_tab": "readers",
        "readers": readers,
        "query": query,
    })

def save_reader(request):
            reader_item = Reader(
                reference_id=request.POST.get('reference_id', ''),
                reader_name=request.POST.get('reader_name', ''),
                reader_contact=request.POST.get('reader_contact', ''),
                reader_address=request.POST.get('reader_address', ''),
                active=True
            )
            reader_item.save()
            return redirect('/readers')

def delete_reader(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)
    reader.delete()
    return redirect('/readers/')



def book_list(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'library/book_list.html', {'books': books})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/')

def add_book(request):
    if request.method == 'POST':
        new_book = Book(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            available_copies=request.POST.get('available_copies'),
            publication_date=request.POST.get('publication_date'),
            isbn=request.POST.get('isbn'),
        )
        new_book.save()
        return redirect('book_list')

    return render(request, 'book_list.html')


def save_book(request):
    print("Request method:", request.method)  # Debugging line
    if request.method == 'POST':
        form = BookForm(request.POST)
        print("Form data:", request.POST)  # Debugging line
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = BookForm()
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'form': form})

def borrowing_list_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book = request.POST.get('book')
        date_borrowed = request.POST.get('date_borrowed')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')

        Borrowing.objects.create(
            name=name,
            book=book,
            date_borrowed=date_borrowed,
            due_date=due_date,
            status=status
        )
        return redirect('borrowing_list_add')

    borrowings = Borrowing.objects.all()
    return render(request, 'create_collection.html', {'borrowings': borrowings})

def delete_borrower(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    if request.method == 'POST':
        borrowing.delete()
    return redirect('borrowing_list_add')