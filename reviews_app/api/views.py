from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews_app.models import Review
from .serializers import ReviewSerializer

class ReviewListCreateView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Nur Authentifizierte können posten, GET ist offen
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['business_user']  # Ermöglicht ?business_user_id=1
    ordering_fields = ['rating', 'created_at']  # Ermöglicht ?ordering=rating oder ?ordering=-created_at

    def get_queryset(self):
        queryset = Review.objects.all()
        business_user_id = self.request.query_params.get('business_user_id')
        if business_user_id:
            queryset = queryset.filter(business_user_id=business_user_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
