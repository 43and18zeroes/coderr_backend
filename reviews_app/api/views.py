from .serializers import ReviewSerializer
from reviews_app.models import Review
from rest_framework.generics import ListAPIView

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
