from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price_stripe_id = models.CharField(max_length=255)
    price = models.IntegerField(default=0) # cents

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('name',)


class Discount(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'


class Tax(models.Model):
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'tax'
        verbose_name_plural = 'taxes'


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(
        Discount,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    tax = models.ForeignKey(
        Tax,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
