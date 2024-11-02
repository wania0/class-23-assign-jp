from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, logout, authenticate
from .models import User
from .serializers import UserSerializer, LoginSerializer

# admin 
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_admin(request : Request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['password'] = make_password(data['password'])
        User.objects.create(user_type = 'admin', **data)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("admin created successfully")

# signup 
@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request : Request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['password'] = make_password(data['password'])
        User.objects.create(user_type = 'reader', **data)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("user register successfully")

# moderator, author
@api_view(['PUT'])
@permission_classes([AllowAny])
def create_moderator_author(request : Request, id):
    data = request.data
    user = User.objects.get(id=id)
    if user is not None:
        user.user_type = data['user_type']  # Update the user type
        user.save()
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("success")

@api_view(['POST'])
def login_view(request:Request):
    data = request.data
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
    
        user = User.objects.get(email=email)  # get user with that email
        if check_password(password, user.password): # check password
            if user is not None:
                login(request, user)
                return Response("user logged in")
            else: 
                return Response("invalid email or password", status=status.HTTP_400_BAD_REQUEST)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

