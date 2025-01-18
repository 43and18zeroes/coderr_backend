from django.urls import path
from .views import CustomLoginView, UserRegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]