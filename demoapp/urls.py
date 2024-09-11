from django.urls import path, include, re_path
from .views import BooksView, BookDetailedView
from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books',BookViewSet)

urlpatterns = [
    # path("", include(router.urls))
    path('api-auth/', include('rest_framework.urls')),
    path("books/", BooksView.as_view(), name="Books"),
    path("book/<int:pk>/", BookDetailedView.as_view(), name="Book"),
    # path("enter/", enter_details, name="enter"),
    # path("book/", BookAuthorView.as_view()),
    # re_path('^book/(?P<author>.+)/$', BookAuthorView.as_view())
]