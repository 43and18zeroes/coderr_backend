from rest_framework import serializers
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["reviewer", "created_at", "updated_at"]

    def validate(self, data):
        request_user = self.context["request"].user
        business_user = data.get("business_user")

        if Review.objects.filter(reviewer=request_user, business_user=business_user).exists():
            raise serializers.ValidationError("Du kannst nur eine Bewertung pro Geschäftsprofil abgeben.")

        return data
