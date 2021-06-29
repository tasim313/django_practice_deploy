"""bohubrihi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from fromapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.from_1, name='singup'),
    path('form_1/', views.form, name='form'),
    path('validator/', views.user_form, name='user_form'),
    path('email/', views.email_validation, name='email'),
    path('customer/', include('fromapp.urls')),
    path('login/', include('loginapp.urls')),
    path('new_app/', include('new_app.urls')),
    path('api_view/', include('API_example.urls')),
]
