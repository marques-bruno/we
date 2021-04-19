from django.db import models
from userauth.models import CustomUser

class Manager(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return self.user.username
