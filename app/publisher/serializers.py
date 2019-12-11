from rest_framework import serializers
from core.models import Publisher


class PublisherSerializers(serializers.ModelSerializer):
    """ Serializer for Publisher """

    class Meta:
        model = Publisher
        fields = "__all__"