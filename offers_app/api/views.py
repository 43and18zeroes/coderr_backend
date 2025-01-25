from rest_framework.generics import ListCreateAPIView
from offers_app.models import Offer
from .serializers import OfferSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['creator_id', 'max_delivery_time']
    filterset_fields = ['user', 'min_delivery_time']
    ordering_fields = ['created_at', 'title']