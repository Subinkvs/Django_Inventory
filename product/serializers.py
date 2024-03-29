from  rest_framework import serializers
from .models import Products, SubVariant, Variant


class SubVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVariant
        fields = '__all__'
        
    
class VariantSerializer(serializers.ModelSerializer):
    options = SubVariantSerializer(many=True, read_only=True)
    
    class Meta:
        model = Variant
        fields = ['id', 'name', 'options']

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)
    
    class Meta:
            model = Products
            fields = ['name' 'variants']