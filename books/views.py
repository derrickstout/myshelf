from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import (PrintBook, EBook, Audiobook)
from django.views.generic import ListView, DetailView

# Create your views here.

def audio(request):
	# prefetching eliminates duplication for querying authors for every item in a loop
	audiobook_list = Audiobook.objects.all().prefetch_related('authors')
	context = {
	'audiobook_list': audiobook_list
	}
	return render(request, 'books/audiobook_list.html', context)


class AudiobookDetail(DetailView):
	model = Audiobook
	template_name = "books/audiobook_detail.html"


# Need to figure out how to pass all book types to single list view
def allBooks(ListView):
	model = PrintBook, Audiobook
	return render(request, template_name='books/book_list.html')


# def index(request):
# 	book_list = Book.objects.all()
# 	# book_list = ', '.join([b.title for b in books])
# 	context = {
# 	'book_list': book_list
# 	}
# 	return render(request, 'books/index.html', context)


# def detail(request, book_id):
# 	try:
# 		book_detail = Book.objects.get(pk=book_id).title, " by ", Book.objects.get(pk=book_id).list_authors()
# 	except Book.DoesNotExist:
# 		raise Http404("This book doesn't seem to exist")
# 	context = {
# 	'book_detail': book_detail
# 	}
# 	return render(request, 'books/detail.html', context)


# class BookList(ListView):
# 	model = Book
# 	#with no template_name specified, Django infers from model and class name "books/book_list.html"


