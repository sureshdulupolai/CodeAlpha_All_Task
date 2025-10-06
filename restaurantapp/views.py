from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import MenuItem, Table, Order, OrderItem

# List menu items
def menu_list(request):
    menu = MenuItem.objects.filter(available=True)
    return render(request, 'restaurant/menu_list.html', {'menu': menu})

# Place an order
def place_order(request):
    if request.method == "POST":
        table_id = request.POST.get('table')
        items = request.POST.getlist('items')  # list of menu_item IDs
        quantities = request.POST.getlist('quantities')  # quantities corresponding

        table = get_object_or_404(Table, id=table_id)
        order = Order.objects.create(table=table)

        for item_id, qty in zip(items, quantities):
            menu_item = get_object_or_404(MenuItem, id=item_id)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=int(qty))

        # Mark table as not available
        table.is_available = False
        table.save()

        return redirect('restaurantapp:order_success', order_id=order.id)

    tables = Table.objects.filter(is_available=True)
    menu = MenuItem.objects.filter(available=True)
    return render(request, 'restaurant/place_order.html', {'tables': tables, 'menu': menu})

# Order success page
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'restaurant/order_success.html', {'order': order})

# API endpoint for menu
def api_menu_list(request):
    menu = list(MenuItem.objects.values('id', 'name', 'description', 'price', 'available'))
    return JsonResponse(menu, safe=False)
