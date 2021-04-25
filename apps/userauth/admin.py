from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'is_supplier', 'is_manager']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture', 'is_supplier', 'is_manager')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)