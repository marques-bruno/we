# Generated by Django 3.0.14 on 2021-04-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20210419_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_supplier',
            field=models.BooleanField(default=False),
        ),
    ]