"""Streamfields live in here."""

from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as tr
from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import MultipleChoiceBlock

from userauth.models import SupplierUser, CustomerUser, ManagerUser
from store import store_models

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

class CardFilterBlock(blocks.StructBlock):
    filter_by = blocks.ChoiceBlock(choices=(
            ("no_sort", tr("Don't sort")),
            ("by_producer", tr("Sort by producer")),
            ("by_type", tr("Sort by type")),
            ("by_labels", tr("Sort by label")),
            ("by_allergens", tr("Sort by allergen")),
            ("by_pickup_point", tr("Sort by Pickup point")),
            ("from_past orders", tr("Show only products this customer already ordered")),
        ),
        default='no_sort',
        help_text=tr('Choose how you want the products filtered'))


    def products_no_sort(self, ctx, products):
        return products;

    def products_by_producer(self, ctx, products):
        return {k: v for k, v in store_models.Product.objects.all().items() if v.supplier == ctx['self']['filters']['by_producer']}

    by_producer = blocks.ChoiceBlock(choices=SupplierUser.objects.all(),
        help_text=tr("Choose which producer's products you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_type '
            'wagtailuiplus__choice-handler-hidden-if--by_label '
            'wagtailuiplus__choice-handler-hidden-if--by_allergens '
            'wagtailuiplus__choice-handler-hidden-if--by_pickup_point '
            'wagtailuiplus__choice-handler-hidden-if--from_past_orders'
        ))

    def products_by_type(self, ctx, products):
        return {k: v for k, v in store_models.Product.objects.all().items() if v.type == ctx['self']['filters']['by_type']}

    by_type = blocks.ChoiceBlock(choices=store_models.ProductType.objects.all(),
        help_text=tr("Choose which type of product you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_producer '
            'wagtailuiplus__choice-handler-hidden-if--by_label '
            'wagtailuiplus__choice-handler-hidden-if--by_allergens '
            'wagtailuiplus__choice-handler-hidden-if--by_pickup_point '
            'wagtailuiplus__choice-handler-hidden-if--from_past_orders'
        ))

    def products_by_labels(self, ctx, products):
        ## todo(@bmarques): Filter by labels (multiple choice field)
        return {k: v for k, v in store_models.Product.objects.all().items() if v.label == ctx['self']['filters']['by_labels']}

    by_labels = MultipleChoiceBlock(choices=store_models.ProductLabel.objects.all(),
        help_text=tr("Choose which product labels you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_type '
            'wagtailuiplus__choice-handler-hidden-if--by_producer '
            'wagtailuiplus__choice-handler-hidden-if--by_allergens '
            'wagtailuiplus__choice-handler-hidden-if--by_pickup_point '
            'wagtailuiplus__choice-handler-hidden-if--from_past_orders'
        ))

    def products_by_allergens(self, ctx, products):
        ## todo(@bmarques): Filter by allergen (multiple choice field)
        return {k: v for k, v in store_models.Product.objects.all().items() if v.allergens == ctx['self']['filters']['by_allergens']}

    by_allergens = MultipleChoiceBlock(choices=store_models.ProductAllergen.objects.all(),
        help_text=tr("Choose which product labels you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_type '
            'wagtailuiplus__choice-handler-hidden-if--by_label '
            'wagtailuiplus__choice-handler-hidden-if--producer '
            'wagtailuiplus__choice-handler-hidden-if--by_pickup_point '
            'wagtailuiplus__choice-handler-hidden-if--from_past_orders'
        ))

    def products_by_pickup_point(self, ctx, products):
        ## @Todo: Filtering products by pickup point is a bit more complicated, let's keep it for later
        return {k: v for k, v in store_models.Product.objects.all().items() if v.type == ctx['self']['filters']['by_type']}

    by_pickup_point = blocks.ChoiceBlock(choices=store_models.PickupPoint.objects.all(),
        help_text=tr("Choose which pickup point products you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_type '
            'wagtailuiplus__choice-handler-hidden-if--by_label '
            'wagtailuiplus__choice-handler-hidden-if--by_allergens '
            'wagtailuiplus__choice-handler-hidden-if--by_producer '
            'wagtailuiplus__choice-handler-hidden-if--from_past_orders'
        ))

    def products_from_past_orders(self, ctx, products):
        ## @Todo: Filtering products from a customer's past orders is a bit more complicated, let's keep it for later
        return {k: v for k, v in store_models.Product.objects.all().items() if v.type == ctx['self']['filters']['by_type']}
        
    by_pickup_point = blocks.ChoiceBlock(choices=store_models.PickupPoint.objects.all(),
        help_text=tr("Choose which pickup point products you want to see"),
        classname=(
            'wagtailuiplus__choice-handler-target--filter_by '
            'wagtailuiplus__choice-handler-hidden-if--no_sort '
            'wagtailuiplus__choice-handler-hidden-if--by_type '
            'wagtailuiplus__choice-handler-hidden-if--by_label '
            'wagtailuiplus__choice-handler-hidden-if--by_allergens '
            'wagtailuiplus__choice-handler-hidden-if--by_producer '
            'wagtailuiplus__choice-handler-hidden-if--by_pickup_point'
        ))


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
    filters = CardFilterBlock()

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
        context['products'] = self.__getattribute__(context['self']['sort_by'])(store_models.Product.objects.all())[:6]
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
