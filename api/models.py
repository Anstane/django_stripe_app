from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price_stripe_id = models.CharField(max_length=255)
    price = models.IntegerField(default=0) # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('name',)


class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in Order {self.order.id}"


# class Order(models.Model):
#     item = models.ForeignKey('Item', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def subtotal(self):
#         return self.item.price * self.quantity

#     def __str__(self):
#         return f'{self.quantity} x {self.item.name}'


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
