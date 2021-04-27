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
    return obj.supplier.user.username
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


@modeladmin_register
class StoreGroup(ModelAdminGroup):
    menu_label = 'Store'
    menu_icon = 'fa-shopping-cart'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (SupplierAdmin, ProductAdmin)

