from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import MenuItem, Table, Order, OrderItem


# 🧾 View Menu List
def menu_list(request):
    menu = MenuItem.objects.filter(available=True)
    return render(request, 'restaurant/menu_list.html', {'menu': menu})


# 🪑 Place Order
def place_order(request):
    tables = Table.objects.filter(is_available=True)
    menu = MenuItem.objects.filter(available=True)

    if request.method == "POST":
        table_id = request.POST.get('table')
        selected_items = request.POST.getlist('items')
        quantities = request.POST.getlist('quantities')

        table = get_object_or_404(Table, id=table_id)
        order = Order.objects.create(table=table)

        for i, item_id in enumerate(selected_items):
            menu_item = MenuItem.objects.get(id=item_id)
            quantity = int(quantities[i])
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        # Mark table as unavailable after placing order
        table.is_available = False
        table.save()

        return render(request, 'restaurant/order_success.html', {'order': order})

    return render(request, 'restaurant/order.html', {'tables': tables, 'menu': menu})


# 📋 View All Orders (Active + Completed)
def view_orders(request):
    active_orders = Order.objects.filter(is_completed=False)
    completed_orders = Order.objects.filter(is_completed=True)
    return render(request, 'restaurant/view_orders.html', {
        'active_orders': active_orders,
        'completed_orders': completed_orders
    })


# ✅ Complete Order
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_completed = True
    order.save()

    # Free up the table
    if order.table:
        order.table.is_available = True
        order.table.save()

    return redirect('restaurantapp:view_orders')


# 📱 API for Menu and Orders (for mobile/frontend use)
def api_menu_list(request):
    menu = list(MenuItem.objects.values('id', 'name', 'price', 'available'))
    return JsonResponse(menu, safe=False)


def api_orders(request):
    orders = list(Order.objects.values('id', 'table__number', 'is_completed', 'created_at'))
    return JsonResponse(orders, safe=False)
