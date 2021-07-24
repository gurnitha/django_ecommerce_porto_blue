# apps/product/views.py

# Django modules
from django.shortcuts import render

# Django locals

# Create your views here.

# Product page views
def product_list(request):
	return render(request, 'product/product-list.html')

# Category page views
def category_list(request):
	return render(request, 'product/category-list.html')