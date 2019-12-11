from rest_framework import serializers
from core.models import Books

class BookSerializers(serializers.ModelSerializer):
    """ Serializer for Book """

    class Meta:
        model = Books
        fields = ('bookname', 'author_name', 'publisher', )