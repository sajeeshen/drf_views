from rest_framework import serializers
from publisher.serializers import PublisherSerializers
from author.serializers import AuthorSerializers
from core.models import Books

class StoreSerializers(serializers.ModelSerializer):
    """ Serializer class for Store """
    publisher = PublisherSerializers(read_only=True)
    author = AuthorSerializers(read_only=True)

    class Meta:
        model = Books
        fields = "__all__"


