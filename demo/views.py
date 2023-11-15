from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from .filters import BookFilter
from .permissions import IsAdminOrReadOnly
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class DemoView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    
    def post(self, request):
        return Response({"message": "Got some data!", "data": request.data})
    

class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, author_id):
        author = Author.objects.get(id=author_id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, author_id):
        author = Author.objects.get(id=author_id)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, author_id):
        author = Author.objects.get(id=author_id)
        author.delete()
        return Response({"message": "Author deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'bio', 'languages__name']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    permission_classes = [IsAdminOrReadOnly]



#write a book review class so that we can track the reviews of a book given by a user
#write a viewset for the book review class
#write a serializer for the book review class
#write a url for the book review class
#write a filter for the book review class
#write a permission for the book review class