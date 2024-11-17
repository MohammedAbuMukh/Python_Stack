from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.root, name='root'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    
    path('books', views.all_books, name='all_books'),
    path('books/<int:id>', views.view_book, name='view_book'),
    path('books/add_book', views.add_book, name='add_book'),
    path('books/edit_book', views.edit_book, name='edit_book'),
    path('books/go_back', views.all_books, name='go_back'),
    path('books/favorite_book_view_all_books/<int:book_id>', views.favorite_book_view_all_books, name='favorite_book_view_all_books'),
    path('books/favorite_book_view_book/<int:book_id>', views.favorite_book_view_book, name='favorite_book_view_book'),
]