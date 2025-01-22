from django.urls import path
from .views import CustomLoginView, UserRegistrationView, UserProfileDetailView

urlpatterns = [
    path('offers/', CustomLoginView.as_view(), name='offers'),
]