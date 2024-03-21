from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {'books':books})

def book_details(request, slug):
    # try:
    # # Here pk represents a primary key field
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # This can also be used for instead of above
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html", {
        'title':book.title,
        'author':book.author,
        'rating':book.rating,
        'is_best_seller':book.is_best_selling
    })