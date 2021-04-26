from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.models import Image

from streams import blocks

class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    max_count = 1

    body = StreamField([
        ("title_and_text", blocks.TitleAndTextBlock()),
        ("cards", blocks.CardBlock()),
        ("richtext", blocks.RichtextBlock()),
        ("simplerichtext", blocks.SimpleRichtextBlock()),
        ("cta", blocks.CTABlock()),
        ("buttons", blocks.ButtonBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]



@register_setting
class SiteSettings(BaseSetting):
    logo = models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='logo')
    panels = [
        ImageChooserPanel('logo'),
    ]