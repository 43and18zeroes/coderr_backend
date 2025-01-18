from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomLoginSerializer, UserRegistrationSerializer

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomLoginView(ObtainAuthToken):
class CustomLoginView(APIView):
    # permission_classes = [AllowAny]
    print('Working')
    
    def post(self, request):
        print('Working Post')
        return Response({'message': 'Temporary response, logic not implemented yet.'})
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