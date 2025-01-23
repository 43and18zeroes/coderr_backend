from .serializers import OfferSerializer
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from offers_app.models import Offer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]  # You can adjust permissions as needed

    def create(self, request, *args, **kwargs):
        """Handle POST requests for creating an Offer."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def update(self, request, *args, **kwargs):
        """Handle PUT requests for updating an Offer."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Handle PATCH requests for partially updating an Offer."""
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)