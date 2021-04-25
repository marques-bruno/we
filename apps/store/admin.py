from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import *

# @modeladmin_register
# class ProductAdmin(ModelAdmin):
#   """ Product admin. """
  
#   model = Product
#   menu_label = "Products"
#   menu_icon = "fa-shopping-basket"
#   menu_order = 290
#   add_to_settings_menu = False
#   exclude_from_explorer = False
#   list_display = ['name', 'product_supplier', ]

#   def product_supplier(self, obj):
#     return obj.supplier.user.username
#   product_supplier.short_description = 'Supplier'
#   product_supplier.admin_order_field = 'product__supplier'


# @modeladmin_register
# class SupplierAdmin(ModelAdmin):
#   """ Supplier admin. """
  
#   model = Supplier
#   menu_label = "Suppliers"
#   menu_icon = "fa-truck"
#   menu_order = 290
#   add_to_settings_menu = False
#   exclude_from_explorer = False
#   list_display = ("user", "address", "phone_number", "email")
#   search_fields = ("user", "address", "phone_number", "email")
