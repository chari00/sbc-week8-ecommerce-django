
# # Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()  # Retrieve all order from the database
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)  # Fetch the orders by ID or return a 404 error if not found
    return render(request, 'orders/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_edit(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

