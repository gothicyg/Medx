""" Defines URL patterns for medx."""
from django.urls import path

from . import views
app_name = 'medx'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # Page that shows all Books.
    path('books/', views.books, name='books'),
    # Detail page for a single book.
    path('books/<int:book_id>/', views.book, name='book'),
    # Page for adding a new book
    path('new_book/', views.new_book, name='new_book'),
    # Page for adding new entry
    path('new_entry/<int:book_id>/', views.new_entry, name='new_entry'),
    #Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]
