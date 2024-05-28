from rest_framework import serializers
from .models import Users, Categories, Products, Orders


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'