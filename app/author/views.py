from .serializers import AuthorSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Author
from django.http import Http404


class AuthorListView(APIView):
    """ List all the Authors """

    def get_objects(self):
        return Author.objects.all()

    def get(self, request):
        """ List all the Authors """
        result = self.get_objects();
        serializers = AuthorSerializers(result, many=True)
        return Response(serializers.data)

    def post(self, request):
        """ Create new Author """
        serializers = AuthorSerializers(data=request.data)
        print(serializers.is_valid())
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class AuthorActionView(APIView):
    """ Class view for managing update / delete etc actions """

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        """ View the details of Author """
        author = self.get_object(pk)
        serializers = AuthorSerializers(author)
        return Response(serializers.data)

    def put(self, request, pk):
        """ Update the specified author"""
        author = self.get_object(pk)
        serializers = AuthorSerializers(author, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ Function for deleting the Author """
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    