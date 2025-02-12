from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user_auth_app.models import UserProfile
from django.conf import settings


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username"
    )
    email = serializers.EmailField(
        source="user.email"
    )
    first_name = serializers.CharField(source="user.first_name", default=None)
    last_name = serializers.CharField(source="user.last_name", default=None)
    file = serializers.ImageField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(source="user.date_joined")

    class Meta:
        model = UserProfile
        fields = [
            "user",
            "username",
            "first_name",
            "last_name",
            "file",
            "location",
            "tel",
            "description",
            "working_hours",
            "type",
            "email",
            "created_at",
        ]
        
    def to_representation(self, instance):
        """Diese Methode fügt die vollständige URL für das Bild hinzu."""
        representation = super().to_representation(instance)
        if instance.file:
            representation["file"] = settings.MEDIA_URL + str(instance.file)
        return representation
        
    def get_file(self, obj):
        if obj.file:
            return settings.MEDIA_URL + str(obj.file)
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=UserProfile.TYPE_CHOICES)

    class Meta:
        model = User
        fields = ["username", "password", "email", "type"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        type = validated_data.pop("type", "customer")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, type=type)
        Token.objects.create(user=user)
        return user


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, data):
        return data

class ProfileByTypeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'file', 'location', 'tel', 'description', 'working_hours', 'type']

    def get_user(self, obj):
        return {
            "pk": obj.user.id,
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }