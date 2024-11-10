from django.contrib import admin

# Register your models here.
from orders.models import Order  # Replace with your model name

class PostAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'quantity', 'order_date')

admin.site.register(Order, PostAdmin)