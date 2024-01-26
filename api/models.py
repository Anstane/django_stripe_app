from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0) # Нужно писать цену с двумя дополнительными нулями.

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('name',)


class Order(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f'{self.quantity} x {self.item.name}'


# class Discount(models.Model):
#     amount = models.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         verbose_name = 'discount'
#         verbose_name_plural = 'discounts'


# class Tax(models.Model):
#     rate = models.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         verbose_name = 'tax'
#         verbose_name_plural = 'taxes'
