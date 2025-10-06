from django.contrib import admin
from .models import MenuItem, Table, Order, OrderItem

# Menu Item Admin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "available")
    list_filter = ("available",)
    search_fields = ("name", "description")
    list_editable = ("available",)

# Table Admin
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "seats", "is_available")
    list_filter = ("is_available",)
    list_editable = ("is_available",)
    ordering = ("number",)

# Inline for Order Items (show inside Orders)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table", "created_at", "is_completed")
    list_filter = ("is_completed", "created_at")
    inlines = [OrderItemInline]
    list_editable = ("is_completed",)
    date_hierarchy = "created_at"

# Order Item Admin (optional standalone view)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity")
    search_fields = ("menu_item__name", "order__id")
