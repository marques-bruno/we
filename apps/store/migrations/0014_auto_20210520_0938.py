# Generated by Django 3.0.14 on 2021-05-20 09:38

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210520_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name', 'supplier']),
        ),
    ]
