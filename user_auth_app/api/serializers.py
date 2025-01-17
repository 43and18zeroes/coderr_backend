from django.contrib.auth.models import User
from rest_framework import serializers
from user_auth_app.models import UserProfile

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('email')
        password = data.get('password')
        
        if username == 'guest@example.com' and password == '123456':
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': 'Guest',
                    'last_name': 'User',
                }
            )
            if created:
                user.set_password(password)
                user.save()

                UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'email': 'guest@example.com',
                        'first_name': 'Guest',
                        'last_name': 'User',
                        'type': 'user_from_signup',
                        'user_color': '#66EB90',
                    }
                )

        #     user = authenticate(username=username, password=password)

        # user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Ungültige E-Mail oder Passwort.")
        
        data['user'] = user
        return data