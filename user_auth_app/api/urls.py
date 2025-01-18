from django.urls import path
from .views import CustomLoginView, UserRegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
]