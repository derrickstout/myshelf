from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
	book_list = Book.objects.all()
	# book_list = ', '.join([b.title for b in books])
	context = {
	'book_list': book_list
	}
	return render(request, 'books/index.html', context)

def detail(request, book_id):
	book_detail = (Book.objects.get(pk=book_id).title, " by ", Book.objects.get(pk=book_id).list_authors())

	return HttpResponse(book_detail)
