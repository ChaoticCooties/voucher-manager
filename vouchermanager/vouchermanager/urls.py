"""vouchermanager URL Configuration

urlpatterns includes backend/frontend includes as well as
the admin site (site-admin/) for separation of concerns. 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('site-admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('', include('vouchers.urls')),
]
