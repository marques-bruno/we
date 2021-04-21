from django.db import models

from userauth.models import ManagerUser
from userauth.models import SupplierUser


class PickupPoint(models.Model):
    """ A Pickup point has a manager and an address assigned to it """
    managers = models.ManyToManyField(ManagerUser, blank=True)
    suppliers = models.ManyToManyField(SupplierUser, blank=True)
    address = models.CharField(max_length=100)
