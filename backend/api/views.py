from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''\
       this is a DRF API view
    '''
    random_product = Product.objects.all().order_by('?').first()
    data= {}
    if random_product:
        data = model_to_dict(random_product, fields=['id','price'])

    return Response(data)

    

