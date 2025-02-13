from rest_framework.permissions import BasePermission
from user_auth_app.models import UserProfile

class IsBusinessUser(BasePermission):
    """
    Permission that allows only users with type 'business' to create an Offer.
    """
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        try:
            return request.user.userprofile.type == "business"
        except UserProfile.DoesNotExist:
            return False
