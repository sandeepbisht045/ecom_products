
from . models import Product
from rest_framework import serializers

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Product
        fields=['id','name','image','details','price']

# product update serializer
class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id']

