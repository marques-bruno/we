# Generated by Django 3.0.14 on 2021-04-22 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
    ]