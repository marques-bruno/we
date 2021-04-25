from django.db import models

class ProductLabel(models.Model):

  ref_name = models.CharField(max_length=32)
  name = models.CharField(max_length=32)
  icon = models.CharField(max_length=512, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Product Label"
    verbose_name_plural = "Product Labels"