from .serializers import OrderSerializer
from orders_app.models import Order
from rest_framework.generics import ListAPIView

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
