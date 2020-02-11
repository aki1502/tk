from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from djoser.serializers import UserSerializer

from ..models import Akeet
from .serializer import AkeetSerializer



class AccountCreateAPIView(views.APIView):
    """アカウント作成APIクラス"""
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(
            username=serializer.initial_data["username"],
            password=serializer.initial_data["password"],
        )
        return Response(serializer.data, status.HTTP_201_CREATED)


class AkeetListCreateAPIView(views.APIView):
    """Akeetの取得(一覧)・投稿APIクラス"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        """Akeetの取得(一覧)"""
        akeets = Akeet.objects.all().order_by("-published_date")[:100]
        serializer = AkeetSerializer(instance=akeets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Akeetの投稿"""
        user = whois(request.META.get("HTTP_AUTHORIZATION").split()[1])
        d = {
            "author": user,
            "text": request.data["text"],
            "published_date": timezone.now()
        }
        Akeet.objects.create(**d)
        return Response({}, status.HTTP_201_CREATED)

def whois(token):
    if not token:
        raise AuthenticationFailed("You need token.")
    try:
        user = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed("invalid token")
    return user.user