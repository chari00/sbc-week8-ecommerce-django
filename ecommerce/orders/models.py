from django import forms
from django.db import models
from django.utils import timezone

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.TextField()
    quantity = models.IntegerField()
    order_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    
    def __str__(self):
    #     return self.title
        return f"{self.customer_name} - {self.product_name}"



class PostForm(forms.ModelForm):
    # Meta class is used to specify the model and fields we want to include in the form.
    class Meta:
        model = Order  # Link the form to the Order model.
        fields = ('customer_name', 'product_name', 'quantity', 'order_date', 'completed')  # Specify the fields we want in the form: 'title' and 'description'.
