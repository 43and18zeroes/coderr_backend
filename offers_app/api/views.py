from rest_framework.pagination import PageNumberPagination
from .serializers import OfferSerializer, OfferDetailSerializer, OfferCreateSerializer, OfferSingleSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from offers_app.models import Offer, OfferDetail
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBusinessUser
from rest_framework.permissions import AllowAny

class OfferPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class OfferFilter(FilterSet):
    creator_id = CharFilter(field_name="user__id")
    max_delivery_time = CharFilter(field_name="min_delivery_time", lookup_expr='lte')

    class Meta:
        model = Offer
        fields = ['creator_id', 'user']


class OfferSingleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSingleSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsBusinessUser()]

class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all().order_by('created_at')
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OfferFilter
    ordering_fields = ['created_at', 'updated_at', 'title', 'min_price', 'min_delivery_time']
    search_fields = ['title', 'description']
    pagination_class = OfferPagination

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated(), IsBusinessUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OfferCreateSerializer
        return OfferSerializer
    
class OfferDetailView(RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer