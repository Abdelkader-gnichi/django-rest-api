from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''\
       this is a DRF API view
    '''
    random_instance = Product.objects.all().order_by('?').first()
    data= {}
    if random_instance:
        serializer= ProductSerializer(random_instance, many=False)
        data = serializer.data

    '''\
        this code bellow will work but will not shows or returns the sale_price
        property that is declared in the product models so here we need to use
        DRF serializers.
    '''
    # if random_product:
    #     data = model_to_dict(random_product, fields=['id','price', 'sale_price']) 

    return Response(data)

    

