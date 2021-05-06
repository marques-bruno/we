from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import *
from userauth.models import SupplierUser, CustomerUser, ManagerUser

class ProductAdmin(ModelAdmin):
  """ Product admin. """
  
  model = Product
  menu_label = "Products"
  menu_icon = "fa-shopping-basket"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = True
  list_display = ('name', 'product_supplier', 'price', 'quantity', 'type', 'labels', 'allergens')
  # list_filter = ('name', 'product_supplier', 'price', 'quantity', 'type', 'labels', 'allergens')
  search_fields = ('name', 'product_supplier', 'quantity', 'type', 'labels', 'allergens')

  def product_supplier(self, obj):
    return obj.supplier.brand_name
  product_supplier.short_description = 'Supplier'
  product_supplier.admin_order_field = 'product__supplier'


class SupplierAdmin(ModelAdmin):
  """ Supplier admin. """
  
  model = SupplierUser
  menu_label = "Suppliers"
  menu_icon = "fa-truck"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = True
  list_display = ("brand_name", "username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")
  # list_filter = ("first_name", "last_name", "city", "zip_code", "country")
  search_fields = ("brand_name", "username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")

  empty_value_display = 'N/A'


class ManagerAdmin(ModelAdmin):
  """ Supplier admin. """
  
  model = ManagerUser
  menu_label = "Managers"
  menu_icon = "fa-address-book-o"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = True
  list_display = ("username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")
  # list_filter = ("first_name", "last_name", "city", "zip_code", "country")
  search_fields = ("username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")

  empty_value_display = 'N/A'


class CustomerAdmin(ModelAdmin):
  """ Supplier admin. """
  
  model = CustomerUser
  menu_label = "Customers"
  menu_icon = "fa-user"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = True
  list_display = ("username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")
  # list_filter = ("first_name", "last_name", "city", "zip_code", "country")
  search_fields = ("username", "email", "first_name", "last_name", "mobile_phone", "address1", "city", "zip_code", "country")

  empty_value_display = 'N/A'


class PickupPointAdmin(ModelAdmin):
  model = PickupPoint
  menu_label = "Pickup Points"
  menu_icon = "fa-map-marker"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = True
  list_display = ("name", "manager_list", "supplier_list", "address")
  # list_filter = ("first_name", "last_name", "city", "zip_code", "country")
  search_fields = ("name", "manager_list", "supplier_list", "address")

  def manager_list(self, obj):
    managers = []
    for manager in obj.managers.all():
      managers.append(manager)
    return managers
  manager_list.short_description = 'Managers'
  manager_list.admin_order_field = 'manager_list'

  def supplier_list(self, obj):
    suppliers = []
    for supplier in obj.suppliers.all():
      suppliers.append(supplier)
    return suppliers
  supplier_list.short_description = 'Suppliers'
  supplier_list.admin_order_field = 'supplier_list'


# class UsersGroup(ModelAdminGroup):
#     menu_label = 'Users'
#     menu_icon = 'fa-users'  # change as required
#     menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
#     items = (SupplierAdmin, ManagerAdmin, CustomerAdmin)
# Nesting of ModelAdminGroups is not permitted yet, in current Wagtail version. Update code when version contains this PR:
# https://github.com/wagtail/wagtail/pull/4571/files


@modeladmin_register
class StoreGroup(ModelAdminGroup):
  menu_label = 'Store'
  menu_icon = 'fa-shopping-cart'  # change as required
  menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
  # items = (UsersGroup, ProductAdmin)
  items = (CustomerAdmin, SupplierAdmin, ManagerAdmin, ProductAdmin, PickupPointAdmin)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
