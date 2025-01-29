from django.contrib.auth.models import User
from offers_app.models import Offer, OfferDetail
from rest_framework import serializers


# class OfferDetailSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField()

#     class Meta:
#         model = OfferDetail
#         fields = ['id', 'url']

#     def get_url(self, obj):
#         return f"/offerdetails/{obj.id}/"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']

class OfferDetailSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    class Meta:
        model = OfferDetail
        fields = ['id', 'title', 'revisions', 'delivery_time_in_days', 'price', 'features', 'offer_type']
        
class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailSerializer(many=True)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        offer = Offer.objects.create(**validated_data)
        
        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)
        
        return offer