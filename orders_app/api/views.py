from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer, OrderSingleSerializer
from orders_app.models import Order
from rest_framework import status
from django.shortcuts import get_object_or_404
from offers_app.models import OfferDetail
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .permissions import OrderPermission

class OrderListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Nur Bestellungen des aktuellen Benutzers anzeigen."""
        return Order.objects.filter(customer_user=self.request.user)

    def create(self, request, *args, **kwargs):
        if not hasattr(request.user, 'userprofile') or request.user.userprofile.type != 'customer':
            return Response({"detail": "Nur Kunden können Bestellungen erstellen."}, status=status.HTTP_403_FORBIDDEN)

        offer_detail_id = request.data.get("offer_detail_id")
        if not offer_detail_id:
            return Response({"non_field_errors": ["offer_detail_id ist erforderlich."]}, status=status.HTTP_400_BAD_REQUEST)

        offer_detail = get_object_or_404(OfferDetail, id=offer_detail_id)

        order_data = {
            "customer_user": request.user.id,
            "business_user": offer_detail.offer.user.id,
            "title": offer_detail.title,
            "revisions": offer_detail.revisions,
            "delivery_time_in_days": offer_detail.delivery_time_in_days,
            "price": offer_detail.price,
            "features": offer_detail.features,
            "offer_type": offer_detail.offer_type,
            "status": "in_progress",
        }

        serializer = self.get_serializer(data=order_data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderSingleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSingleSerializer
    permission_classes = [IsAuthenticated, OrderPermission]
    
class OrderCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id, *args, **kwargs):
        
        if not User.objects.filter(id=business_user_id).exists():
            return Response({"error": "Business user not found."}, status=404)
        
        order_count = Order.objects.filter(business_user_id=business_user_id, status='in_progress').count()
        return Response({"order_count": order_count})
    
class CompletedOrderCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id, *args, **kwargs):
        
        if not User.objects.filter(id=business_user_id).exists():
            return Response({"error": "Business user not found."}, status=404)

        completed_order_count = Order.objects.filter(
            business_user_id=business_user_id,
            status='completed'
        ).count()
        return Response({"completed_order_count": completed_order_count})