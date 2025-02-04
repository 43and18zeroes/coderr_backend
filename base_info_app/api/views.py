from django.db import models
from rest_framework.views import APIView
from base_info_app.models import BaseInfo
from .serializers import BaseInfoSerializer
from rest_framework.response import Response
from reviews_app.models import Review
from user_auth_app.models import UserProfile
from offers_app.models import Offer


class BaseInfoView(APIView):
    def get(self, request, *args, **kwargs):
        review_count = Review.objects.count()  # Zählt alle Reviews
        average_rating = Review.objects.aggregate(models.Avg('rating'))['rating__avg'] or 0.0  # Durchschnittswert der Bewertungen
        business_profile_count = UserProfile.objects.filter(type="business").count()  # Anzahl Business-Profile
        offer_count = Offer.objects.count()  # Anzahl der Angebote

        data = {
            "review_count": review_count,
            "average_rating": round(average_rating, 2),  # Rundet den Durchschnitt
            "business_profile_count": business_profile_count,
            "offer_count": offer_count
        }

        return Response(data)