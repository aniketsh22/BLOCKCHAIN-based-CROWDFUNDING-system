"""CFDAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from CF import views
from django.contrib import admin
from django.urls import path
from CF import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('connect', views.connect, name='connect'),
    path('my_redirect', views.my_redirect, name='my_redirect'),
    path('signin', views.signin, name='signin'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('project', views.project, name='project'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('donate1', views.donate1, name='donate1'),
    path('donate2', views.donate2, name='donate2'),
    path('donate3', views.donate3, name='donate3'),
]
