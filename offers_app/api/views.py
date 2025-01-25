from .serializers import OfferSerializer
from django_filters.rest_framework import DjangoFilterBackend
from offers_app.models import Offer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView


class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['creator_id', 'max_delivery_time']
    filterset_fields = ['user', 'min_delivery_time']
    ordering_fields = ['created_at', 'title']