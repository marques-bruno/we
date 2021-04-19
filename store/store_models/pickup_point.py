from django.db import models

from .manager import Manager
from .supplier import Supplier


class PickupPoint(models.Model):
    """ A Pickup point has a manager and an address assigned to it """
    managers = models.ManyToManyField(Manager, blank=True)
    suppliers = models.ManyToManyField(Supplier, blank=True)
    address = models.CharField(max_length=100)
