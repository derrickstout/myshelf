from django.urls import path
from books.views import BookList

from . import views

app_name = 'books'
urlpatterns = [
	path('', BookList.as_view()),
	path('<int:book_id>/', views.detail, name='detail'),
]