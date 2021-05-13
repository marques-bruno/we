from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as tr

from .models import User, Address

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'birthdate', 'is_supplier', 'is_manager', 'is_staff')

admin.site.register(User, UserAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'first_name', 'last_name', 'address1', 'address2', 'city', 'country', 'mobile_phone', 'phone', 'is_primary')
    pass

admin.site.register(Address, AddressAdmin)
