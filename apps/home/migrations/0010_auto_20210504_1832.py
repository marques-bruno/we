# Generated by Django 3.0.14 on 2021-05-04 18:32

from django.db import migrations
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210504_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('products', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, required=False)), ('sort_by', wagtail.core.blocks.ChoiceBlock(choices=[('no_sort', "Don't sort"), ('most_recent', 'Most Recently added'), ('best_sellers', 'Best sellers'), ('your favorites', 'Best sellers')], help_text='Choose how you want the products sorted')), ('filters', wagtail.core.blocks.StructBlock([('filter_by', wagtail.core.blocks.ChoiceBlock(choices=[('no_sort', "Don't sort"), ('by_producer', 'Sort by producer'), ('by_type', 'Sort by type'), ('by_labels', 'Sort by label'), ('by_allergens', 'Sort by allergen'), ('by_pickup_point', 'Sort by Pickup point'), ('from_past_orders', 'Show only products this customer already ordered')], classname='wagtailuiplus__choice-handler wagtailuiplus__choice-handler--filter_by', help_text='Choose how you want the products filtered')), ('by_producer', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--no_sort wagtailuiplus__choice-handler-hidden-if--by_type wagtailuiplus__choice-handler-hidden-if--by_labels wagtailuiplus__choice-handler-hidden-if--by_allergens wagtailuiplus__choice-handler-hidden-if--by_pickup_point wagtailuiplus__choice-handler-hidden-if--from_past_orders', help_text="Choose which producer's products you want to see")), ('by_type', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--no_sort wagtailuiplus__choice-handler-hidden-if--by_producer wagtailuiplus__choice-handler-hidden-if--by_labels wagtailuiplus__choice-handler-hidden-if--by_allergens wagtailuiplus__choice-handler-hidden-if--by_pickup_point wagtailuiplus__choice-handler-hidden-if--from_past_orders', help_text='Choose which type of product you want to see')), ('by_labels', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--no_sort wagtailuiplus__choice-handler-hidden-if--by_type wagtailuiplus__choice-handler-hidden-if--by_producer wagtailuiplus__choice-handler-hidden-if--by_allergens wagtailuiplus__choice-handler-hidden-if--by_pickup_point wagtailuiplus__choice-handler-hidden-if--from_past_orders', help_text='Choose which product labels you want to see')), ('by_allergens', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--no_sort wagtailuiplus__choice-handler-hidden-if--by_type wagtailuiplus__choice-handler-hidden-if--by_labels wagtailuiplus__choice-handler-hidden-if--by_producer wagtailuiplus__choice-handler-hidden-if--by_pickup_point wagtailuiplus__choice-handler-hidden-if--from_past_orders', help_text='Choose which product labels you want to see')), ('by_pickup_point', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--no_sort wagtailuiplus__choice-handler-hidden-if--by_type wagtailuiplus__choice-handler-hidden-if--by_labels wagtailuiplus__choice-handler-hidden-if--by_allergens wagtailuiplus__choice-handler-hidden-if--by_producer wagtailuiplus__choice-handler-hidden-if--by_pickup_point', help_text='Choose which pickup point products you want to see'))])), ('max_cards', wagtail.core.blocks.IntegerBlock(help_text='Number of cards to display on the page section (max. 6)', max_value=6))])), ('cta', wagtail.core.blocks.StructBlock([('bg_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.CharBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=True))])), ('nested_stream_field', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, required=False)), ('filters', wagtail.core.blocks.StreamBlock([('by_supplier', wagtail.core.blocks.ChoiceBlock(choices=[], help_text="Choose which producer's products you want to see")), ('by_type', wagtail.core.blocks.ChoiceBlock(choices=[], help_text='Choose which type of product you want to see'))], max_num=1))]))], blank=True, null=True),
        ),
    ]
