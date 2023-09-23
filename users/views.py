from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password  # For password hashing
from .models import User
from .serializers import UserSerializer  # Import your serializer

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                user_data = serializer.validated_data

                # Hash the password before saving it
                user_data['password'] = make_password(user_data['password'])

                # Create or get the user by email
                user, created = User.objects.get_or_create(email=user_data['email'], defaults=user_data)
                
                if not created:
                    return JsonResponse({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

                return JsonResponse({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            email = request.GET.get('email', '')
            password = request.GET.get('password', '')

            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email=email)

                # Check the password using Django's check_password function
                if check_password(password, user.password):
                    serializer = UserSerializer(user)
                    return JsonResponse(serializer.data)
                else:
                    return JsonResponse({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


