from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=32)