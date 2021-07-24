# apps/main/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.main.views import home 

# Appp name
app_name = "mani"

urlpatterns = [
    path('', home, name="home"),
]
