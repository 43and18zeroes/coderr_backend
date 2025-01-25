from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user_auth_app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username"
    )
    email = serializers.EmailField(
        source="user.email"
    )
    first_name = serializers.CharField(source="user.first_name", default=None)
    last_name = serializers.CharField(source="user.last_name", default=None)
    created_at = serializers.DateTimeField(source="user.date_joined")

    class Meta:
        model = UserProfile
        fields = [
            "id",
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
        # username = data.get('email')
        # password = data.get('password')

        # if username == 'guest@example.com' and password == '123456':
        #     user, created = User.objects.get_or_create(
        #         username=username,
        #         defaults={
        #             'first_name': 'Guest',
        #             'last_name': 'User',
        #         }
        #     )
        #     if created:
        #         user.set_password(password)
        #         user.save()

        #         UserProfile.objects.get_or_create(
        #             user=user,
        #             defaults={
        #                 'email': 'guest@example.com',
        #                 'first_name': 'Guest',
        #                 'last_name': 'User',
        #                 'type': 'user_from_signup',
        #                 'user_color': '#66EB90',
        #             }
        #         )

        #     user = authenticate(username=username, password=password)

        # user = authenticate(username=username, password=password)
        # if not user:
        #     raise serializers.ValidationError("Ungültige E-Mail oder Passwort.")

        # data['user'] = user
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