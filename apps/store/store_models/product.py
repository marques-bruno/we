from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.shortcuts import reverse

from wagtail.admin.edit_handlers import RichTextField

from userauth.models import SupplierUser

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
    slug = AutoSlugField(
        populate_from=["name", "supplier"],
    )
    supplier = models.ForeignKey(SupplierUser, on_delete=models.CASCADE, null=False, blank=False, default=None)
    price = models.FloatField(default=9999.99)
    quantity = models.PositiveIntegerField(default=0)
    quantity_per_unit = models.FloatField(default=1)
    unit = models.ForeignKey(ProductUnit, blank=False, null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(ProductType, blank=False, null=True, on_delete=models.SET_NULL)

    labels = models.ManyToManyField(ProductLabel, blank=True)
    allergens = models.ManyToManyField(ProductAllergen, blank=True)
    
    description = RichTextField(null=True, blank=True, default="Fresh, local, fair price.")
    farmers_advice = RichTextField(null=True, blank=True)
    image = models.ImageField(default=None)


    def get_absolute_url(self):
        return reverse("store:product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("store:add_to_cart", kwargs={'slug': self.slug})

    def get_add_to_cart_url_next(self):
        return reverse("store:add_to_cart_next", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.pk) + ' ' + self.name

