from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as tr
from django_countries.fields import CountryField
from django.conf import settings
from django.template.defaulttags import register
from django.db import transaction

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(verbose_name=tr("First name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name=tr("Last name"), max_length=30, blank=True, null=True)
    address1 = models.CharField(verbose_name=tr("Address line 1"), max_length=250, blank=True, null=True)
    address2 = models.CharField(verbose_name=tr("Address line 2"), max_length=250, blank=True, null=True)
    zip_code = models.CharField(verbose_name=tr("Postal Code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=tr("City"), max_length=150, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=tr("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=tr("Mobile phone"), max_length=17, blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], verbose_name=tr("Phone"), max_length=17, blank=True, null=True)
    additional_information = models.CharField(verbose_name=tr("Additional information"), max_length=4096, blank=True, null=True)
    is_primary = models.BooleanField(verbose_name=tr("Primary address"), default="False", blank=True)
    name = models.CharField(verbose_name=tr("Name"), max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        ## is_primary is *distinct* field. if primary==True,
        ##  need to remove flag from other entries
        primary_addresses = Address.objects.filter(user=self.user, is_primary=True)
        if not self.is_primary:
            if primary_addresses.count():
                return super(Address, self).save(*args, **kwargs)
            else:
                self.is_primary=True
                return super(Address, self).save(*args, **kwargs)
        with transaction.atomic():
            primary_addresses.update(is_primary=False)
            return super(Address, self).save(*args, **kwargs)  
          
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class User(AbstractUser):
    birthdate = models.DateField(verbose_name=tr("Date of birth"), blank=True, null=True)
    picture = models.ImageField(verbose_name=tr("Profile Picture"), upload_to='profile_pics/', default='profile_pics/default-user-avatar.png')

    is_supplier = models.BooleanField(blank=False, default=False)
    is_manager = models.BooleanField(blank=False, default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_addresses(self):
        return Address.objects.filter(user=self)

    @property
    def has_primary_address(self):
        return Address.objects.filter(user=self, is_primary=True).count()


    @property
    def has_address(self):
        return Address.objects.filter(user=self).count()


    def get_address_primary(self):
        addr = Address.objects.filter(user=self, is_primary=True)
        if addr.count():
            return addr[0]
        return Address(user=None, is_primary=False)

    @property
    def address1(self):
        return self.get_address_primary().address1

    @property
    def address2(self):
        return self.get_address_primary().address2

    @property
    def city(self):
        return self.get_address_primary().city

    @property
    def zip_code(self):
        return self.get_address_primary().zip_code

    @property
    def country(self):
        return self.get_address_primary().country

    @property
    def mobile_phone(self):
        return self.get_address_primary().mobile_phone

    @property
    def phone(self):
        return self.get_address_primary().phone

    @property
    def additional_information(self):
        return self.get_address_primary().additional_information


    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"



class CustomerUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def username(self):
        return self.user.username
    username.short_description = 'User name'

    def email(self):
        return self.user.email
    email.short_description = 'Email'

    def birthdate(self):
        return self.user.birthdate
    birthdate.short_description = 'Birth date'

    def picture(self):
        return self.user.picture
    picture.short_description = 'avatar'

    def first_name(self):
        return self.user.first_name
    first_name.short_description = 'First name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'Last name'

    def address1(self):
        return self.user.address1
    address1.short_description = 'Address 1'

    def address2(self):
        return self.user.address2
    address2.short_description = 'Address 2'

    def city(self):
        return self.user.city
    city.short_description = 'City'

    def zip_code(self):
        return self.user.zip_code
    zip_code.short_description = 'Zip code'

    def country(self):
        return self.user.country
    country.short_description = 'Country'

    def mobile_phone(self):
        return self.user.mobile_phone
    mobile_phone.short_description = 'Mobile phone'

    def phone(self):
        return self.user.phone
    mobile_phone.short_description = 'Phone'

    def additional_information(self):
        return self.user.additional_information
    additional_information.short_description = 'Additional information'

 
    def __str__(self):
        f"{self.user.username} {self.user.first_name} {self.user.last_name}"


    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class SupplierUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brand_name = models.CharField(verbose_name=tr("Brand name"), max_length=100, blank=True, null=True)

    def username(self):
        return self.user.username
    username.short_description = 'User name'

    def email(self):
        return self.user.email
    email.short_description = 'Email'

    def birthdate(self):
        return self.user.birthdate
    birthdate.short_description = 'Birth date'

    def picture(self):
        return self.user.picture
    picture.short_description = 'avatar'

    def first_name(self):
        return self.user.first_name
    first_name.short_description = 'First name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'Last name'

    def address1(self):
        return self.user.address1
    address1.short_description = 'Address 1'

    def address2(self):
        return self.user.address2
    address2.short_description = 'Address 2'

    def city(self):
        return self.user.city
    city.short_description = 'City'

    def zip_code(self):
        return self.user.zip_code
    zip_code.short_description = 'Zip code'

    def country(self):
        return self.user.country
    country.short_description = 'Country'

    def mobile_phone(self):
        return self.user.mobile_phone
    mobile_phone.short_description = 'Mobile phone'

    def phone(self):
        return self.user.phone
    mobile_phone.short_description = 'Phone'

    def additional_information(self):
        return self.user.additional_information
    additional_information.short_description = 'Additional information'

 
    def __str__(self):
        return f"{self.brand_name}: {self.user.first_name} {self.user.last_name}"

 
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"


class ManagerUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def username(self):
        return self.user.username
    username.short_description = 'User name'

    def email(self):
        return self.user.email
    email.short_description = 'Email'

    def birthdate(self):
        return self.user.birthdate
    birthdate.short_description = 'Birth date'

    def picture(self):
        return self.user.picture
    picture.short_description = 'avatar'

    def first_name(self):
        return self.user.first_name
    first_name.short_description = 'First name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'Last name'

    def address1(self):
        return self.user.address1
    address1.short_description = 'Address 1'

    def address2(self):
        return self.user.address2
    address2.short_description = 'Address 2'

    def city(self):
        return self.user.city
    city.short_description = 'City'

    def zip_code(self):
        return self.user.zip_code
    zip_code.short_description = 'Zip code'

    def country(self):
        return self.user.country
    country.short_description = 'Country'

    def mobile_phone(self):
        return self.user.mobile_phone
    mobile_phone.short_description = 'Mobile phone'

    def phone(self):
        return self.user.phone
    mobile_phone.short_description = 'Phone'

    def additional_information(self):
        return self.user.additional_information
    additional_information.short_description = 'Additional information'

    def __str__(self):
        return f"{self.username}: {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

