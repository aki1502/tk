from rest_framework import serializers

from ..models import Akeet



class AkeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akeet
        fields = (
            "author",
            "text",
            "published_date",
        )