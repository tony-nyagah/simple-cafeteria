from rest_framework import serializers

from .models import Customer, FoodItem, Order


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("id", "name", "description", "price", "image")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer", "items", "total_price", "status")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")
