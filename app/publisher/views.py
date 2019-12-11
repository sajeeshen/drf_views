from rest_framework import viewsets
from core.models import Publisher
from .serializers import PublisherSerializers


class PublisherViewSet(viewsets.ModelViewSet):
    """ View set for Publisher """
    serializer_class = PublisherSerializers
    queryset = Publisher.objects.all()
