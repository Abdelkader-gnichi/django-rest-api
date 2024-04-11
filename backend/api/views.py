from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    '''\
       this is a DRF API view
    '''
    
    '''\
        the serializer is used for validating the request data if it is matching
        the serializer requirements then the model requirements and/or to save
        the request data into the database.

        if we don't use the save method then we only validating the request data 
        without saving anything into the database.
    '''
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True): # raise_exception it's like serializer.errors
        # instance = serializer.save()s
        return Response(serializer.data)

    

