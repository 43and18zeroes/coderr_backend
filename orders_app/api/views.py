from .serializers import OfferSerializer
from orders_app.models import Offer
from rest_framework.generics import ListAPIView

class OfferListView(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
