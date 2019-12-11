from rest_framework import serializers
from core.models import  Author


class AuthorSerializers(serializers.ModelSerializer):
    """" Serializers for Author """

    class Meta:
        model = Author
        fields = ('name',)