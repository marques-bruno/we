from django.db import models

class ProductUnit(models.Model):

    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Unit"
        verbose_name_plural = "Product Units"