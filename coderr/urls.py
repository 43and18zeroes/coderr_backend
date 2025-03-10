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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from base_info_app.api.views import BaseInfoView
from offers_app.api.views import OfferListCreateAPIView, OfferSingleAPIView, OfferDetailView
from orders_app.api.views import OrderListCreateView, OrderSingleAPIView, OrderCountView, CompletedOrderCountView
from reviews_app.api.views import ReviewListCreateView, ReviewSingleView
from user_auth_app.api.views import CustomLoginView, UserRegistrationView, ProfileByTypeListView, ProfileSingleAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/offers/', OfferListCreateAPIView.as_view(), name='offer-list-create'),
    path('api/offers/<int:pk>/', OfferSingleAPIView.as_view(), name='offer-single'),
    path('api/offerdetails/<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderSingleAPIView.as_view(), name='order-single'),
    path('api/order-count/<int:business_user_id>/', OrderCountView.as_view(), name='order-count'),
    path('api/completed-order-count/<int:business_user_id>/', CompletedOrderCountView.as_view(), name='completed-order-count'),
    path("api/base-info/", BaseInfoView.as_view(), name="base-info"),
    path('api/profile/<int:pk>/', ProfileSingleAPIView.as_view(), name='user-profile-detail'),
    path('api/profiles/<str:type>/', ProfileByTypeListView.as_view(), name='profiles'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path("api/reviews/<int:pk>/", ReviewSingleView.as_view(), name="review-single"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()