from rest_framework.permissions import BasePermission

class OrderPermission(BasePermission):
    """
    Erlaubt das Erstellen von Orders nur für Kunden (customer),
    während Bearbeitung und Löschung nur für Geschäftsbenutzer (business) erlaubt sind.
    """

    def has_permission(self, request, view):
        # Nutzer muss eingeloggt sein
        if not request.user.is_authenticated:
            return False
        
        # Zugriff auf `userprofile` sicherstellen
        if not hasattr(request.user, 'userprofile'):
            return False

        user_type = request.user.userprofile.type

        # POST (erstellen) nur für "customer"
        if request.method == "POST":
            return user_type == "customer"

        # PATCH & DELETE (bearbeiten/löschen) nur für "business"
        if request.method in ["PATCH", "DELETE"]:
            return user_type == "business"

        # GET, HEAD, OPTIONS für alle authentifizierten Nutzer erlaubt
        return True
