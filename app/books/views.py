from rest_framework import generics, mixins
from core.models import Books
from .serializers import BookSerializers
from rest_framework.response import Response
from rest_framework import status



class BookList(generics.ListCreateAPIView):
    """ API View for listing and createing new Book """
    queryset = Books.objects.all()
    serializer_class = BookSerializers


class BookUpdateView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """ API View for Updating the Book object """
    queryset = Books.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        """ Get the details about the Book """
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        """ Update the Book object """
        return self.update(request, pk)

    def delete(self, request, pk):
        """ Delete Book object """
        return self.destroy(request, pk)
        