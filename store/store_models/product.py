from django.db import models
from wagtail.admin.edit_handlers import RichTextField

from .supplier import Supplier
from .product_unit import ProductUnit
from .product_type import ProductType
from .product_label import ProductLabel
from .product_allergen import ProductAllergen

class Product(models.Model):
    """
        A product has a mandatory name, supplier, price, quantity, quantity_per_unit and a unit field.
        Optionally, an image can be assigned to it, along with a descriptive text provided by the supplier
        Join tables include ProductLabel, ProductType and ProductAllergen
    """
    name = models.CharField(max_length=200, null=False, blank=False, default=None)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=False, blank=False, default=None)
    price = models.FloatField(default=9999.99)
    quantity = models.IntegerField(default=0)
    quantity_per_unit = models.FloatField(default=1)
    unit = models.ForeignKey(ProductUnit, blank=False, null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(ProductType, blank=False, null=True, on_delete=models.SET_NULL)

    labels = models.ManyToManyField(ProductLabel, blank=True)
    allergens = models.ManyToManyField(ProductAllergen, blank=True)
    
    description = RichTextField(null=True, blank=True, default="Fresh, local, fair price.")
    farmers_advice = RichTextField(null=True, blank=True)
    image = models.ImageField(default=None)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

