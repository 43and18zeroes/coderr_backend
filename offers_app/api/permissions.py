from rest_framework.permissions import BasePermission
from user_auth_app.models import UserProfile

class IsBusinessUser(BasePermission):
    """
    Permission that allows only users with type 'business' to create an Offer.
    """
    
    def has_permission(self, request, view):
        # Allow GET requests for all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Ensure the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Check if the user has a UserProfile and is a 'business'
        try:
            return request.user.userprofile.type == "business"
        except UserProfile.DoesNotExist:
            return False
