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

# class OrderListCreateView(ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Sicherstellen, dass der Benutzer ein CustomerProfile hat
        if not hasattr(request.user, 'userprofile') or request.user.userprofile.type != 'customer':
            return Response({"error": "Nur Kunden können Bestellungen erstellen."}, status=status.HTTP_403_FORBIDDEN)

        # offer_detail_id aus der Anfrage extrahieren
        offer_detail_id = request.data.get("offer_detail_id")
        if not offer_detail_id:
            return Response({"error": "offer_detail_id ist erforderlich."}, status=status.HTTP_400_BAD_REQUEST)

        # OfferDetail abrufen oder Fehler zurückgeben
        offer_detail = get_object_or_404(OfferDetail, id=offer_detail_id)

        # Bestelldaten aus OfferDetail übernehmen
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

        # Bestellung erstellen
        serializer = self.get_serializer(data=order_data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderSingleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSingleSerializer
    
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
        # Überprüfen, ob der Business-User existiert
        if not User.objects.filter(id=business_user_id).exists():
            return Response({"error": "Business user not found."}, status=404)

        # Bestellungen mit Status "completed" zählen
        completed_order_count = Order.objects.filter(
            business_user_id=business_user_id,
            status='completed'
        ).count()
        return Response({"completed_order_count": completed_order_count})