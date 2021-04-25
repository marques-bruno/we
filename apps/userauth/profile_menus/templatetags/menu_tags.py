from django import template

from ..models import ProfileMenu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    try:
        return ProfileMenu.objects.get(slug=slug)
    except ProfileMenuItem.DoesNotExist:
        return ProfileMenu.objects.none()