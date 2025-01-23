"""
URL configuration for coderr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_auth_app.api.views import CustomLoginView, UserRegistrationView, UserProfileDetailView
from offers_app.api.views import OfferView, OfferDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('user_auth_app.api.urls')),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('api/offers/', OfferView.as_view(), name='offer-view'),
    path('api/offers/<int:pk>/', OfferDetailView.as_view(), name='offer-view-detail'),
]
