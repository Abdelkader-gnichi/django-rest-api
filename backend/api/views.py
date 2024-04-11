from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
# Create your views here.

def api_home(request, *args, **kwargs):

    random_product = Product.objects.all().order_by('?').first()

    data= {}
    if random_product:
        data['id'] = random_product.id
        data['title'] = random_product.title
        data['content'] = random_product.content
        data['price'] = random_product.price

    # model instance (random_product)
    # put its content into a dict | turn it into a dict
    # return JSON response contains that dict to my client
    
    return JsonResponse(data)

