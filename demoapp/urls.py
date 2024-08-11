from django.urls import path
from .views import list_books, enter_details, BooksView

urlpatterns = [
    path("books/", BooksView.as_view(), name="Books"),
    path("enter/", enter_details, name="enter"),
]