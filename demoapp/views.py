from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.http import HttpResponse, JsonResponse
# from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from django.views import View
from .models import Book

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import mixins, generics
from .permissions import IsAdminOrReadOnly

# Create your views here.
# python manage.py createsuperuser

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BooksView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# class BooksView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BookDetailedView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class BooksView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         book_serializer = BookSerializer(books, many=True)
#         # return HttpResponse(book_serializer.data)
#         return Response(book_serializer.data, status=status.HTTP_200_OK)
    
#     # def get()
    
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             # print("Data validated")
#             serializer.save()
#             return Response("Data added to db successfully", status=status.HTTP_201_CREATED)
#         else:
#             return Response("please enter valid Data", status=status.HTTP_406_NOT_ACCEPTABLE)

# class BookDetailedView(APIView):

#     def get(self, request, book_id):
#         # book = Book.objects.filter(id=book_id)
#         book = get_object_or_404(Book, pk=book_id)
#         book_serializer = BookSerializer(book)
#         print(book_serializer.data)
#         return JsonResponse(book_serializer.data)

# def enter_details(request):

#     return render(request, 'form.html')

# @api_view(['GET', 'POST'])
# def list_books(request):

#     if request.method == "GET":
#         books = Book.objects.all()
#         book_serializer = BookSerializer(books, many=True)
#         return HttpResponse(book_serializer.data)
#     elif request.method == "POST":
        
#         # t = request.POST.get('title')
#         # a = request.POST.get("author")
#         # p = request.POST.get("price")
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             # print("Data validated")
#             serializer.save()
#             return HttpResponse("Data added to db successfully")
#         else:
#             return HttpResponse("please enter valid Data")

        # print(title, author, price)
        # Book.objects.create(title=t, author=a, price=p )
        # print(request.data)

        # return HttpResponse("POST method invo`ked")

    
    # return HttpResponse("TESTING")
    


# localhost:port/books
