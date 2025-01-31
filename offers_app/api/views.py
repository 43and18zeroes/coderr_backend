from rest_framework.pagination import PageNumberPagination
from .serializers import OfferSerializer, OfferDetailSerializer, OfferCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from offers_app.models import Offer, OfferDetail
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class OfferPagination(PageNumberPagination):
    page_size = 10


class OfferFilter(FilterSet):
    creator_id = CharFilter(field_name="user__id")

    class Meta:
        model = Offer
        fields = ['creator_id', 'user']


class OfferSingleAPIView(RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all().order_by('-created_at')
    # serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OfferFilter
    ordering_fields = ['created_at', 'title']
    search_fields = ['title', 'description']
    pagination_class = OfferPagination
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OfferCreateSerializer  # 👈 Verwende den neuen Serializer für POST
        return OfferSerializer  # 👈 Standard-Serializer für GET
    
class OfferDetailView(RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer