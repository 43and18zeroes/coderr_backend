from .serializers import OfferSerializer, OfferDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from offers_app.models import Offer, OfferDetail
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class OfferFilter(FilterSet):
    creator_id = CharFilter(field_name="user__id")

    class Meta:
        model = Offer
        fields = ['creator_id', 'user', 'min_delivery_time', 'max_delivery_time']
        
class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OfferFilter  # Filter für User und Lieferzeit
    ordering_fields = ['created_at', 'title']  # Sortierung nach Erstellungsdatum und Titel
    search_fields = ['title', 'description']  # Suchfunktion nach Titel oder Beschreibung
    
class OfferDetailRetrieveAPIView(RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer


# class OfferListCreateAPIView(ListCreateAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
#     filterset_fields = ['creator_id', 'max_delivery_time']
#     filterset_fields = ['user', 'min_delivery_time']
#     ordering_fields = ['created_at', 'title']