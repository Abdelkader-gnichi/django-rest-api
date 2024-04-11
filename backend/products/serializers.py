from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'discount']
    
    def get_discount(self, obj):
        # this code is useful when we don't save anything to the DB using the serializer like that 
        # we don't have any obj instance, so we can't reach anything is related to the model stuff
        # like huhu() here
        if not hasattr(obj,'id') or not isinstance(obj, Product):
            return None
        
        # obj is the instance of the serialized object, so we can do what ever 
        # we want to do with it 
        return obj.huhu()