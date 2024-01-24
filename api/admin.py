from django.contrib import admin

from .models import (Item, Order)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'price_stripe_id',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_items',
        'total_amount',
    )
    list_select_related = ('items',)

    def display_items(self, obj):
        items_list = [f"{item.quantity} x {item.item.name}" for item in obj.orderitem_set.all()]
        return ", ".join(items_list)

    display_items.short_description = 'Items'

    def total_amount(self, obj):
        return obj.calculate_total()

    total_amount.short_description = 'Total Amount'
    total_amount.admin_order_field = 'calculate_total'


# @admin.register(models.Discount)
# class DiscountAdmin(admin.ModelAdmin):
#     list_display = (
#         'amount',
#     )


# @admin.register(models.Tax)
# class TaxAdmin(admin.ModelAdmin):
#     list_display = (
#         'rate',
#     )
