from .serializers import CustomLoginSerializer, UserRegistrationSerializer, UserProfileSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user_auth_app.models import UserProfile

User = get_user_model()

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class CustomLoginView(APIView):
    SPECIAL_USERS = {
        "andrey": {
            "password": "asdasd",
            "email": "customer@example.com",
            "type": "customer"
        },
        "kevin": {
            "password": "asdasd24",
            "email": "business@example.com",
            "type": "business"
        }
    }

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username in self.SPECIAL_USERS and password == self.SPECIAL_USERS[username]["password"]:
            user_data = self.SPECIAL_USERS[username]
            user, created = User.objects.get_or_create(
                username=username, 
                defaults={"email": user_data["email"]}
            )
            if created:
                user.set_password(password)
                user.save()
                UserProfile.objects.create(user=user, type=user_data["type"])

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

# class CustomLoginView(ObtainAuthToken):
# class CustomLoginView(APIView):
    # permission_classes = [AllowAny]
    # print('Working')
    
    # def post(self, request):
    #     print('Working Post')
        # return Response({'message': 'Temporary response, logic not implemented yet.'})
        # serializer = CustomLoginSerializer(data=request.data)
        
        # data = {}
        # if serializer.is_valid():
        #     user = serializer.validated_data['user']
        #     # token, created = Token.objects.get_or_create(user=user)
        #     data = {
        #         # 'token': token.key,
        #         'username': user.username,
        #     }
        # else:
        #     # data=serializer.errors
        #     pass
            
        # return Response(data)