from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as tr
from django_countries.fields import CountryField

class CustomUser(AbstractUser):

    birthdate = models.DateField(verbose_name=tr("Date of birth"), blank=True, null=True)
    address1 = models.CharField(verbose_name=tr("Address line 1"), max_length=250, blank=True, null=True)
    address2 = models.CharField(verbose_name=tr("Address line 2"), max_length=250, blank=True, null=True)
    zip_code = models.CharField(verbose_name=tr("Postal Code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=tr("City"), max_length=150, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=tr("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=tr("Mobile phone"), max_length=17, blank=True, null=True)
    additional_information = models.CharField(verbose_name=tr("Additional information"), max_length=4096, blank=True, null=True)
    picture = models.ImageField(verbose_name=tr("Profile Picture"), upload_to='profile_pics/', default='profile_pics/default-user-avatar.png')

    is_supplier = models.BooleanField(blank=False, default=False)
    is_manager = models.BooleanField(blank=False, default=False)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"