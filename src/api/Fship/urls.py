"""Fship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from fship_app.serializers import CustomJWTSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('fship/', include('fship_app.urls')),
    # Path to obtain a new access and refresh token
    path('token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer)),
    # Submit your refresh token to this path to obtain a new access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
