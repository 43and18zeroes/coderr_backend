from rest_framework.generics import ListAPIView
from reviews_app.models import Review
from .serializers import ReviewSerializer

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
