from django.urls import path
from . import views

app_name = 'restaurantapp'

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('order/', views.place_order, name='place_order'),
    path('orders/', views.view_orders, name='view_orders'),
    path('orders/<int:order_id>/complete/', views.complete_order, name='complete_order'),
    path('api/menu/', views.api_menu_list, name='api_menu_list'),
    path('api/orders/', views.api_orders, name='api_orders'),
]
