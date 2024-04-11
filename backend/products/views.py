from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # instances that you want to deals with
    serializer_class = ProductSerializer # the serializer that will be used 

    lookup_field = 'pk' # this how to specify the lookup column in the DB

class ProductCreateAPIView(generics.CreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    # if you want to override the perform_create method (only if you have extra logic)
    def perform_create(self, serializer):
        # if self.request.user:
        #     serializer.save(user= self.request.user) 

        # as a dummy logic we assign the title to the content var if it's None
        title= serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content == None:
            content = title 
        serializer.save(content=content)

        # Send Django Signal here (use case that force you to override perform_create())


