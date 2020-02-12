import base64

from django.core.files import File
from rest_framework import serializers

from ..models import Akeet, UserInfo



class AkeetSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Akeet
        fields = (
            "author",
            "text",
            "published_date",
        )

    def get_author(self, obj):
        return obj.author.username

class UserInfoSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = UserInfo
        fields = (
            "base64_image",
            "vio",
        )

    def get_base64_image(self, obj):
        with open(obj.image.path, "rb") as f:
            image = File(f)
            data = base64.b64encode(image.read())
        return data