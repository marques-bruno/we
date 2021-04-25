from django import template

from ..profile_menus.models import ProfileMenu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    # import pudb; pu.db()
    try:
        objs = ProfileMenu.objects
        slogubj = ProfileMenu.objects.get(slug=slug)
        return ProfileMenu.objects.get(slug=slug)
    except ProfileMenuItem.DoesNotExist:
        return ProfileMenu.objects.none()