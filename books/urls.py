from django.urls import path
from books.views import BookList
from django.contrib.auth import views as auth_views 

from . import views

app_name = 'books'
urlpatterns = [
	path('', BookList.as_view(), name='book-list'),
	path('logout/', auth_views.logout, { 'next_page': 'books:login' }, name='logout'),
	path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
	path('<int:book_id>/', views.detail, name='detail'),
]