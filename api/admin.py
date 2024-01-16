from django.contrib import admin

from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'amount',
    )


@admin.register(models.Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = (
        'rate',
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'display_items',
        'discount',
        'tax',
    )

    def display_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
