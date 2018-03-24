from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .import views

app_name = 'users'

urlpatterns = [
	path('index/', views.create_user, name = 'index'),
	path('rest-index/', views.CreateUser.as_view(), name = 'rest-index'),
]