from rest_framework.response import Response
from .serializers import CustomLoginSerializer

# class CustomLoginView(ObtainAuthToken):
class CustomLoginView():
    # permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # token, created = Token.objects.get_or_create(user=user)
            data = {
                # 'token': token.key,
                'username': user.username,
            }
        else:
            # data=serializer.errors
            pass
            
        return Response(data)