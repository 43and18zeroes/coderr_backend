from rest_framework.pagination import PageNumberPagination
from .serializers import OfferSerializer, OfferDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from offers_app.models import Offer, OfferDetail
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class OfferPagination(PageNumberPagination):
    page_size = 10  # Anzahl der Objekte pro Seite


class OfferFilter(FilterSet):
    creator_id = CharFilter(field_name="user__id")

    class Meta:
        model = Offer
        fields = ['creator_id', 'user', 'min_delivery_time', 'max_delivery_time']


class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OfferFilter
    ordering_fields = ['created_at', 'title']
    search_fields = ['title', 'description']
    pagination_class = OfferPagination

class OfferDetailAPIView(RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
