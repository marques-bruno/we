from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ProfileMenu, ProfileMenuItem


@modeladmin_register
class MenuAdmin(ModelAdmin):
    model = ProfileMenu
    menu_label = "ProfileMenus"
    menu_icon = "list-ul"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
