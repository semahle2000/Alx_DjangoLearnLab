from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class TestView(APIView):
    def get(self, request):
        return Response({"message": "Django REST Framework is working!"}, status=status.HTTP_200_OK)

    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView handles creating a new book.
    - POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView handles updating a book by ID.
    - PUT: Update a book by ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView handles deleting a book by ID.
    - DELETE: Delete a book by ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class BookListView(generics.ListCreateAPIView):
    """
    BookListView handles listing all books and creating a new book.
    - GET: List all books.
    - POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    BookDetailView handles retrieving, updating, and deleting a book by ID.
    - GET: Retrieve a book by ID.
    - PUT: Update a book by ID (authenticated users only).
    - DELETE: Delete a book by ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]