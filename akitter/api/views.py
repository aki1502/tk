from rest_framework import status, views
from rest_framework.response import Response

from ..models import Akeet
from .serializer import AkeetSerializer



class AkeetListAPIView(views.APIView):
    """Akeetの取得(一覧)APIクラス"""

    def get(self, request, *args, **kwargs):
        """Akeetの取得(一覧)"""
        akeets = Akeet.objects.all().order_by("-published_date")[:100]
        serializer = AkeetSerializer(instance=akeets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)