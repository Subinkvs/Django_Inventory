from django.urls import path
from .views import ProductListCreateAPIView, AddStockAPIView, RemoveStockAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('add-stock/<uuid:pk>', AddStockAPIView.as_view(), name='add-stock'),
    path('remove-stock/<uuid:pk>', RemoveStockAPIView.as_view(), name="remove-stock")
]
