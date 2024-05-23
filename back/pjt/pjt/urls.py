"""
URL configuration for pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/join/', include('dj_rest_auth.registration.urls')),
    path('articles/', include('articles.urls')), 
    path('accounts/getuser/<str:username>/', views.getuser), 
    path('accounts/makeusers/', views.makeusers), 
    path('accounts/getallusers/', views.allusers), 
    path('products/', include('products.urls')), 
    path('exchanges/', include('exchanges.urls')), 
    path('gpt/', include('gpt.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
