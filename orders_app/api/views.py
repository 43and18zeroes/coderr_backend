from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer
from orders_app.models import Order

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer