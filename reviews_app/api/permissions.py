from rest_framework.permissions import BasePermission
from user_auth_app.models import UserProfile

class IsCustomerAndReviewerOrReadOnly(BasePermission):
    """
    Erlaubt GET für alle.
    Erlaubt PATCH und DELETE nur für Kunden, die gleichzeitig die Ersteller der Bewertung sind.
    """
    def has_object_permission(self, request, view, obj):
        # GET ist für alle erlaubt
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        # Benutzer muss eingeloggt sein
        if not request.user.is_authenticated:
            return False
        
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return False
        
        # Nur Kunden, die die Review verfasst haben, dürfen PATCH und DELETE ausführen
        if user_profile.type == "customer" and obj.reviewer == request.user:
            return True
        
        return False
