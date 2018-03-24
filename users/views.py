from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from users.serializers import UserSerializer

def create_user(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)

		return JsonResponse(serializer.data, status=200, safe=False)

	if request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class CreateUser(generics.CreateAPIView):
	serializer_class = UserSerializer
