from django.urls import path
from . import views

app_name = 'restaurantapp'

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('order/', views.place_order, name='place_order'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('api/menu/', views.api_menu_list, name='api_menu_list'),
]
