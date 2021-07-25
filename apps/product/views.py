# apps/product/views.py

# Django modules
from django.shortcuts import render, get_object_or_404

# Django locals
from apps.product.models import Category, Product

# Create your views here.

# Product page views
def product_list(request, category_slug=None):
	
	category = None
	categories = Category.objects.all()
	
	products = Product.objects.filter(available=True)
	# print(products)
	
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	context = {
		'category': category,
		'categories': categories,
		'products': products
	}

	# print(categories)
	return render(request, 'product/product-list.html', context)

