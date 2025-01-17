from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView, name='login'),
]