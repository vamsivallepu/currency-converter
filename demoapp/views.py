from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from django.views import View
from .models import Book

# Create your views here.
# python manage.py createsuperuser

class BooksView(View):

    def get(self, request):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return HttpResponse(book_serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # print("Data validated")
            serializer.save()
            return HttpResponse("Data added to db successfully")
        else:
            return HttpResponse("please enter valid Data")

def enter_details(request):

    return render(request, 'form.html')

@api_view(['GET', 'POST'])
def list_books(request):

    if request.method == "GET":
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return HttpResponse(book_serializer.data)
    elif request.method == "POST":
        
        # t = request.POST.get('title')
        # a = request.POST.get("author")
        # p = request.POST.get("price")
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # print("Data validated")
            serializer.save()
            return HttpResponse("Data added to db successfully")
        else:
            return HttpResponse("please enter valid Data")

        # print(title, author, price)
        # Book.objects.create(title=t, author=a, price=p )
        # print(request.data)

        # return HttpResponse("POST method invo`ked")

    
    # return HttpResponse("TESTING")
    


# localhost:port/books
