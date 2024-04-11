from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request, *args, **kwargs):

    random_product = Product.objects.all().order_by('?').first()

    data= {}
    if random_product:
        data = model_to_dict(random_product, fields=['id','price'])

    return JsonResponse(data)

    '''\
        all this commented part will cause an error because here i want to convert 
        the data (which is a dict) variable into a json string type in order to send it as a 
        HttpResponse to my client, even changing the header type manually to application/json will 
        not solve the problem.
    '''
        # print(data)
        # data = dict(data) # this will not gonna help because the data var is actually a dict 
        # data = json.dumps(data) # convert the dict into json string type

    # return HttpResponse(data, headers={"content-type":'application/json'})

