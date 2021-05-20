# Generated by Django 3.0.14 on 2021-05-04 15:29

from django.db import migrations
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210504_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('products', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, required=False)), ('sort_by', wagtail.core.blocks.ChoiceBlock(choices=[('no_sort', "Don't sort"), ('most_recent', 'Most Recently added'), ('best_sellers', 'Best sellers'), ('your favorites', 'Best sellers')], help_text='Choose how you want the products sorted')), ('filters', wagtail.core.blocks.StructBlock([('filter_by', wagtail.core.blocks.ChoiceBlock(choices=[('nosort', "Don't sort"), ('byproducer', 'Sort by producer'), ('bytype', 'Sort by type'), ('bylabels', 'Sort by label'), ('byallergens', 'Sort by allergen'), ('bypickuppoint', 'Sort by Pickup point'), ('frompastorders', 'Show only products this customer already ordered')], help_text='Choose how you want the products filtered')), ('by_producer', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--nosort wagtailuiplus__choice-handler-hidden-if--bytype wagtailuiplus__choice-handler-hidden-if--bylabels wagtailuiplus__choice-handler-hidden-if--byallergens wagtailuiplus__choice-handler-hidden-if--bypickuppoint wagtailuiplus__choice-handler-hidden-if--frompastorders', help_text="Choose which producer's products you want to see")), ('by_type', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--nosort wagtailuiplus__choice-handler-hidden-if--byproducer wagtailuiplus__choice-handler-hidden-if--bylabels wagtailuiplus__choice-handler-hidden-if--byallergens wagtailuiplus__choice-handler-hidden-if--bypickuppoint wagtailuiplus__choice-handler-hidden-if--frompastorders', help_text='Choose which type of product you want to see')), ('by_labels', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--nosort wagtailuiplus__choice-handler-hidden-if--bytype wagtailuiplus__choice-handler-hidden-if--byproducer wagtailuiplus__choice-handler-hidden-if--byallergens wagtailuiplus__choice-handler-hidden-if--bypickuppoint wagtailuiplus__choice-handler-hidden-if--frompastorders', help_text='Choose which product labels you want to see')), ('by_allergens', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--nosort wagtailuiplus__choice-handler-hidden-if--bytype wagtailuiplus__choice-handler-hidden-if--bylabels wagtailuiplus__choice-handler-hidden-if--byproducer wagtailuiplus__choice-handler-hidden-if--bypickuppoint wagtailuiplus__choice-handler-hidden-if--frompastorders', help_text='Choose which product labels you want to see')), ('by_pickup_point', wagtail.core.blocks.ChoiceBlock(choices=[], classname='wagtailuiplus__choice-handler-target--filter_by wagtailuiplus__choice-handler-hidden-if--nosort wagtailuiplus__choice-handler-hidden-if--bytype wagtailuiplus__choice-handler-hidden-if--bylabels wagtailuiplus__choice-handler-hidden-if--byallergens wagtailuiplus__choice-handler-hidden-if--byproducer wagtailuiplus__choice-handler-hidden-if--bypickuppoint', help_text='Choose which pickup point products you want to see'))])), ('max_cards', wagtail.core.blocks.IntegerBlock(help_text='Number of cards to display on the page section (max. 6)', max_value=6))])), ('richtext', streams.blocks.RichtextBlock()), ('simplerichtext', streams.blocks.SimpleRichtextBlock()), ('cta', wagtail.core.blocks.StructBlock([('bg_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.CharBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=True))])), ('buttons', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))]))], blank=True, null=True),
        ),
    ]
