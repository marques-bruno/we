from django import template

from userprofile.models import ProfileMenu, ProfileMenuItem

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