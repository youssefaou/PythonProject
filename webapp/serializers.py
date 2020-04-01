from rest_framework import serializers
from . models import products


class productsSerializer(serializers.ModelSerializer):

    class Meta:
        model  = products
        field=('product_id','product_name')
        fields = '__all__'
