from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer
from orders_app.models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id, *args, **kwargs):
        order_count = Order.objects.filter(business_user_id=business_user_id).count()
        return Response({"order_count": order_count})