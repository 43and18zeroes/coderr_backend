from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomLoginSerializer

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