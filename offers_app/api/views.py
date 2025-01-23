from rest_framework.generics import ListCreateAPIView
from offers_app.models import Offer
from .serializers import OfferSerializer


class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer