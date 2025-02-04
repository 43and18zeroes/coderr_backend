from base_info_app.models import BaseInfo
from rest_framework import serializers

class BaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseInfo
        fields = ['review_count', 'average_rating', 'business_profile_count', 'offer_count']