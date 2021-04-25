from django.db import models

from .product import Product
from .order import Order


class OrderItem(models.Model):
    """ The ProductItem table links a product to an order, assigns a quantity and a date, matching the time the item was placed in the basket """
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=False, default=1)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE, default=None)
    date_added = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
