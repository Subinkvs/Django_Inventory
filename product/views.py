from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Products, Variant, SubVariant
from .serializers import ProductSerializer, VariantSerializer, SubVariantSerializer
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
     def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            product_data = serializer.validated_data
            variants_data = product_data.pop('variants')
            product = Products.objects.create(**product_data)
            
            for variant_data in variants_data:
                options_data = variant_data.pop('options')
                variant = Variant.objects.create(product=product, **variant_data)
                
                for option_data in options_data:
                    SubVariant.objects.create(variant=variant, **option_data)
                    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AddStockAPIView(generics.UpdateAPIView):
    queryset = Variant.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_stock = request.data.get('new_stock')
        instance.stock += new_stock
        instance.save()
        return Response("Stock added successfully")
    
class RemoveStockAPIView(generics.UpdateAPIView):
    queryset = Variant.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        sold_stock =request.data.get('sold_stock')
        instance.stock -= sold_stock
        return Response("Stock removed successfully")
