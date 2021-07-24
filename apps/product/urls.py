# apps/product/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.product.views import product_list 

# Appp name
app_name = "product"

urlpatterns = [
    path('product-list', product_list, name="product-list"),
]
