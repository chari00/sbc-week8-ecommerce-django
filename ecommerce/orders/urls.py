from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('order/new/', views.order_create, name='order_create'),
    path('order/<int:id>/edit/', views.order_edit, name='order_edit'),
    path('order/<int:id>/delete/', views.order_delete, name='order_delete'),
]