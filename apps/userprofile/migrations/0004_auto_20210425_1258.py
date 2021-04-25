# Generated by Django 3.0.14 on 2021-04-25 12:58

from django.conf import settings
from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0046_auto_20210425_0828'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('userprofile', '0003_accoutinfopage_dashboardpage_favoritefarmerspage_messageboardpage_pastorderspage_pendingorderspage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteFarmersPage',
            new_name='AccountInfoPage',
        ),
        migrations.RenameModel(
            old_name='AccoutInfoPage',
            new_name='FavouriteFarmersPage',
        ),
        migrations.RemoveField(
            model_name='profilemenuitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='profilemenuitem',
            name='link_title',
        ),
        migrations.RemoveField(
            model_name='profilemenuitem',
            name='link_url',
        ),
        migrations.AddField(
            model_name='profilemenuitem',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='page'),
        ),
        migrations.DeleteModel(
            name='MessageBoardPage',
        ),
    ]
