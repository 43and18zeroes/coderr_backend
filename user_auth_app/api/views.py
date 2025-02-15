from .serializers import (
    CustomLoginSerializer,
    UserRegistrationSerializer,
    UserProfileSerializer,
    ProfileByTypeSerializer,
)
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user_auth_app.models import UserProfile
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                    "user_id": user.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileSingleAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        """Alle authentifizierten Nutzer dürfen auf alle Profile zugreifen."""
        return UserProfile.objects.all()


class CustomLoginView(APIView):
    SPECIAL_USERS = {
        "andrey": {
            "password": "asdasd",
            "email": "customer@example.com",
            "type": "customer",
        },
        "kevin": {
            "password": "asdasd24",
            "email": "business@example.com",
            "type": "business",
        },
    }

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response(
                {"error": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if self.is_special_user(username, password):
            self.handle_special_user(username, password)

        user = authenticate(username=username, password=password)
        if user:
            return self.generate_response(user)

        return Response(
            {"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
        )

    def is_special_user(self, username, password):
        return (
            username in self.SPECIAL_USERS
            and password == self.SPECIAL_USERS[username]["password"]
        )

    def handle_special_user(self, username, password):
        user_data = self.SPECIAL_USERS[username]
        user, created = User.objects.get_or_create(
            username=username, defaults={"email": user_data["email"]}
        )
        if created:
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, type=user_data["type"])

    def generate_response(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id,
            },
            status=status.HTTP_200_OK,
        )


class ProfileByTypeListView(ListAPIView):
    serializer_class = ProfileByTypeSerializer

    def get_queryset(self):
        profile_type = self.kwargs.get("type")
        if profile_type not in ["business", "customer"]:
            raise NotFound("Invalid profile type.")
        return UserProfile.objects.filter(type=profile_type)