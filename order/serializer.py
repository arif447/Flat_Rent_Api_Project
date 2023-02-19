from rest_framework import serializers
from order.models import Cart, Order
from Account.models import User_create
from flat.models import Flat



class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['user', 'item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_items', 'user', 'paymentId', 'OrderId']


