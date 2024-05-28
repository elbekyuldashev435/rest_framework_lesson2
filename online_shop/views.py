from django.shortcuts import render
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users, Categories, Products, Orders
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def get_user(request, pk):
    user = Users.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = Users.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def update_user(request, pk):
    user = Users.objects.get(pk=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)