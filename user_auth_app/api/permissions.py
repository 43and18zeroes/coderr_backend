from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow GET access for everyone,
    but restrict editing to the profile owner.
    """
    
    def has_permission(self, request, view):
        # GET, HEAD und OPTIONS sind für alle erlaubt
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # GET, HEAD und OPTIONS für alle, Änderungen nur für den Besitzer
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user