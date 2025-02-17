from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from reviews_app.models import Review
from .permissions import IsCustomerAndReviewerOrReadOnly
from .serializers import ReviewSerializer
from user_auth_app.models import UserProfile
from rest_framework.exceptions import PermissionDenied

class ReviewListCreateView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["business_user", "reviewer"]
    ordering_fields = ["rating", "created_at"]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.type != "customer":
            raise PermissionDenied("Nur Kunden können Bewertungen erstellen.")

        reviewer_id = self.request.data.get("reviewer")
        if reviewer_id and reviewer_id != self.request.user.id:
            raise PermissionDenied("Du kannst keine Bewertung im Namen eines anderen Nutzers abgeben.")

        serializer.save(reviewer=self.request.user)

class ReviewSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsCustomerAndReviewerOrReadOnly]