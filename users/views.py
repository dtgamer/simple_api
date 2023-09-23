from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                user_data = serializer.validated_data
                user, created = User.objects.get_or_create(email=user_data['email'], defaults=user_data)
                if not created:
                    return JsonResponse({'error': 'User with this email already exists.'}, status=400)

                return JsonResponse({'message': 'User created successfully.'}, status=201)
            else:
                return JsonResponse({'errors': serializer.errors}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get(self, request):
        try:
            email = request.GET.get('email', '')
            password = request.GET.get('password', '')

            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            try:
                user = User.objects.get(email=email, password=password)
                serializer = UserSerializer(user)
                return JsonResponse(serializer.data)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found.'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

