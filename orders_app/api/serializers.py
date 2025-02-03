from rest_framework import serializers
from orders_app.models import Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'customer_user',
            'business_user',
            'title',
            'revisions',
            'delivery_time_in_days',
            'price',
            'features',
            'offer_type',
            'status',
            'created_at',
            'updated_at',
        ]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_revisions(self, value):
        if value < 0:
            raise serializers.ValidationError("Revisions cannot be negative.")
        return value

class OrderSingleSerializer(serializers.ModelSerializer):
    customer_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    business_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    features = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Order
        fields = [
            'id', 'customer_user', 'business_user', 'title', 'revisions', 'delivery_time_in_days',
            'price', 'features', 'offer_type', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_revisions(self, value):
        if value < 0:
            raise serializers.ValidationError("Revisions cannot be negative.")
        return value

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance