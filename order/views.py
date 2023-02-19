from django.shortcuts import render
from rest_framework.response import Response
from order.models import Cart, Order
from order.serializer import OrderSerializer, CartSerializer
from rest_framework import generics, mixins

# Create your views here.

class add_cart(generics.ListCreateAPIView):
    """Cart create api"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class update_cart(generics.RetrieveUpdateAPIView, mixins.DestroyModelMixin):
    """Cart update api"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class make_order(generics.ListCreateAPIView):
    """order create api"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class update_order(generics.RetrieveUpdateAPIView, mixins.DestroyModelMixin):
    """order update api"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
