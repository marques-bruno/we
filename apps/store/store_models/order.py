from django.db import models

from userauth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_started = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_items(self):
        from store.models import OrderItem
        return OrderItem.objects.filter(order=self)

    @property
    def get_cart_total(self):
        orderitems = self.get_items.all()
        return round(sum([item.get_total for item in orderitems]), 2)
        

    def __str__(self):
        return str(self.id)
        
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

