from .forms import UserUpdateForm

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, PageChooserPanel
)
from wagtail.core.models import Page
from wagtail.core.models import Orderable

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from django import forms

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from django_extensions.db.fields import AutoSlugField

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
    
)

class ProfileMenuItem(Orderable):
    url = models.CharField(max_length=100, default="/", help_text="the relative url of the target page")
    title = models.CharField(max_length=30, default="")

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
    ]

    page = ParentalKey("ProfileMenu", related_name="menu_items")


class ProfileMenu(ClusterableModel):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Menu Item"),
    ]

    def __str__(self):
        menu_items = ProfileMenu.objects.get(slug=self.slug).menu_items.all()
        return self.title + ' - ' + str([item.title for item in menu_items])

