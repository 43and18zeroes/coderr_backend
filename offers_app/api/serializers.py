from django.contrib.auth.models import User
from offers_app.models import Offer, OfferDetail
from rest_framework import serializers


class OfferDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = OfferDetail
        fields = ['id', 'url']

    def get_url(self, obj):
        return f"/offerdetails/{obj.id}/"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']

class OfferSerializer(serializers.ModelSerializer):
    creator_id = serializers.SerializerMethodField()
    user_details = UserSerializer(source='user', read_only=True)
    details = OfferDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = [
            'id',
            'creator_id',
            'user',
            'title',
            'description',
            'created_at',
            'updated_at',
            'details',
            'min_price',
            'min_delivery_time',
            'max_delivery_time',
            'user_details',
        ]
        
    def get_creator_id(self, obj):
        # Gibt die ID des Benutzers zurück
        return obj.user.id if obj.user else None

    def get_user_details(self, obj):
        # Benutzerdetails (z.B. für Name und Username)
        if obj.user:
            return {
                "first_name": obj.user.first_name,
                "last_name": obj.user.last_name,
                "username": obj.user.username,
            }
        return None

    def get_details(self, obj):
        # Details des Angebots (URLs)
        return [{"id": detail.id, "url": f"/offerdetails/{detail.id}/"} for detail in obj.details.all()]