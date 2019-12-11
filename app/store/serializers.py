from rest_framework import serializers
from publisher.serializers import PublisherSerializers
from author.serializers import AuthorSerializers


class StoreSerializers(serializers.Serializer):
    """ Serializer class for Store """
    publisher = PublisherSerializers(read_only=True)
    author = AuthorSerializers(read_only=True)


