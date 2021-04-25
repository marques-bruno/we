from .forms import UserUpdateForm

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, PageChooserPanel
)
from wagtail.core.models import Page
from wagtail.core.models import Orderable

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

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


class DashboardPage(Page):
    template = "dashboard.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tab'] = "dashboard"
        return context


class AccountInfoPage(Page):
    template = "account_info.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['form'] = UserUpdateForm
        context['tab'] = "account-information"
        return context


class PendingOrdersPage(Page):
    template = "pending_orders.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tab'] = "pending-orders"
        return context


class PastOrdersPage(Page):
    template = "past_orders.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tab'] = "past-orders"
        return context


class FavoriteFarmersPage(Page):
    template = "favorite_farmers.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tab'] = "favorite-farmers"
        return context


class MessageBoardPage(Page):
    template = "message_board.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tab'] = "message-board"
        return context


class ProfileMenuItem(Orderable):
    def slugified(content):
        import pudb; pu.db()
        return content.title

    item_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )
    slug = models.CharField(max_length=30, help_text="Must be the Item Page's slug")

    panels = [
        PageChooserPanel("item_page"),
        FieldPanel("slug"),
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
        return self.title
