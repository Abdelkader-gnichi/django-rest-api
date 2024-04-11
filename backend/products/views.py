from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # instances that you want to deals with
    serializer_class = ProductSerializer # the serializer that will be used 

    lookup_field = 'pk' # this how to specify the lookup column in the DB
    