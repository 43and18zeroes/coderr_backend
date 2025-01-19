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
            # Erstelle einen Token für den Benutzer
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,  # Authentifizierungstoken
                "user_id": user.id,  # Benutzer-ID
                "username": user.username,  # Benutzername
                "message": "User registered successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Spezielle Prüfung für den Benutzer "andrey"
        if username == "andrey" and password == "asdasd":
            user, created = User.objects.get_or_create(username="andrey")
            if created:
                user.set_password(password)
                user.save()

            # Benutzer authentifizieren
            user = authenticate(username=username, password=password)
            if user:
                # Token erstellen oder abrufen
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "token": token.key,
                    "user_id": user.id,
                    "username": user.username,
                    "message": "Login erfolgreich." if not created else "Benutzer erstellt und eingeloggt."
                }, status=status.HTTP_200_OK)
            return Response({"error": "Fehler beim Login."}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Standard-Login-Logik für andere Benutzer
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "message": "Login erfolgreich."
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