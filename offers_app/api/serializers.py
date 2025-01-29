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
    min_price = serializers.FloatField(read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'created_at', 'details', 'min_price']

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        offer = Offer.objects.create(**validated_data)

        min_price = None
        for detail_data in details_data:
            detail = OfferDetail.objects.create(offer=offer, **detail_data)
            if min_price is None or detail.price < min_price:
                min_price = detail.price

        offer.min_price = min_price if min_price is not None else 0.0
        offer.save(update_fields=['min_price'])

        return offer  