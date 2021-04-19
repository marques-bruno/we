from django.db import models

class ProductType(models.Model):

    ref_name = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    icon = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"