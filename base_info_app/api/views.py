from rest_framework.views import APIView
from base_info_app.models import BaseInfo
from .serializers import BaseInfoSerializer
from rest_framework.response import Response


class BaseInfoView(APIView):
    def get(self, request, *args, **kwargs):
        stats, created = BaseInfo.objects.get_or_create(id=1)  # Sicherstellen, dass ein Datensatz existiert
        serializer = BaseInfoSerializer(stats)
        return Response(serializer.data)