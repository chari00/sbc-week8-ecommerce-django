from django.contrib import admin

# Register your models here.
from .models import Order  # Replace with your model name

admin.site.register(Order)