# apps/main/views.py

# Django modules
from django.shortcuts import render

# Django locals

# Create your views here.

# Home page views
def home(request):
	return render(request, 'main/index.html')