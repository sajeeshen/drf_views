from rest_framework import viewsets
from core.models import Books
from .serializers import StoreSerializers


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """ Viewset for Store API """
    queryset = Books.objects.all()
    serializer_class = StoreSerializers
