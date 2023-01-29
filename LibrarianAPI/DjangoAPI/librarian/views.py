from django.http import JsonResponse
from .models import Librarian
from .serializers import LibrarianSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST','POST','DELETE'])
def librarian_list (request, format=None):
    if request.method == 'GET':
        books = Librarian.objects.all()
        # serializer = LibrarianSerializer(books, many=True)
        # return JsonResponse(serializer.data, safe=True)
        # return JsonResponse({"books": serializer.data})
        serializer = LibrarianSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','DELETE','PUT'])
def librarian_detail(request, id, format=None):
    try:
        book = Librarian.objects.get(pk=id)
    except Librarian.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LibrarianSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LibrarianSerializer(book, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

