# Generated by Django 3.0.14 on 2021-05-07 08:16

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210506_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name', 'supplier']),
        ),
    ]