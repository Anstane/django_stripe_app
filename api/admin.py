from django.contrib import admin

from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_items',
        'total_amount',
    )

    def display_items(self, obj):
        items_list = [f"{obj.quantity} x {obj.item.name}"]
        return ", ".join(items_list)

    def total_amount(self, obj):
        total_price = obj.item.price * obj.quantity
        return "{0:.2f}".format(total_price / 100)



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
