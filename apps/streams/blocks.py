"""Streamfields live in here."""

from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as tr
from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
import store

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text=tr("Add your title"))
    text = blocks.TextBlock(required=True, help_text=tr("Add additional text"))

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = tr("Title & Text")


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text=tr("Add your title"))
    bg_image = ImageChooserBlock(required=False, blank=False, null=True, on_delete=models.SET_NULL)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text=tr("If the button page above is selected, that will be used first."),  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = tr("Staff Cards")



class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )


class ProductCardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text=tr("Add your title"))
    bg_image = ImageChooserBlock(required=False, blank=False, null=True, on_delete=models.SET_NULL)
    sort_by = RadioSelectBlock(choices=(
            ("no_sort", tr("Don't sort")),
            ("most_recent", tr("Most Recently added")),
            ("best_sellers", tr("Best sellers")),
            ("your favorites", tr("Best sellers")),
        ),
        default='no_sort',
        help_text=tr('Choose how you want the products sorted'))
    filter_by = blocks.ChoiceBlock(choices=(
            ("no_sort", tr("Don't sort")),
            ("producer", tr("Sort by producer")),
            ("type", tr("Sort by type")),
            ("label", tr("Sort by label")),
            ("pickup_point", tr("Sort by Pickup point")),
            ("already_ordered", tr("Show only products this customer already ordered")),
        ),
        default='no_sort',
        help_text=tr('Choose how you want the products filtered'))

    max_cards = blocks.IntegerBlock(max_value=6, help_text=tr("Number of cards to display on the page section (max. 6)"))

    def no_sort(self, products):
        return products

    def most_recent(self, products):
        return sorted(products, key=lambda x: x.id, reverse=True)

    def best_sellers(self, products):
        # Todo: fetch orders, add together the number of sales for each item, store it in a table and sort accordingly
        return sorted(products, key=lambda x: x)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = self.__getattribute__(context['self']['sort_by'])(store.models.Product.objects.all())[:6]
        return context

    class Meta:  # noqa
        template = "streams/product_cards_block.html"
        icon = "placeholder"
        label = tr("Product Cards block")



class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    bg_image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""

    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #     return context

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue
