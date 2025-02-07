from rest_framework.permissions import BasePermission

class IsReviewerOrAdmin(BasePermission):
    """
    Erlaubt PATCH & DELETE nur dem Ersteller der Bewertung oder einem Admin.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.reviewer or request.user.is_staff
