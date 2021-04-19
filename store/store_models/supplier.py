from django.db import models
from userauth.models import CustomUser
from wagtail.admin.edit_handlers import RichTextField


class Supplier(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.user.username


