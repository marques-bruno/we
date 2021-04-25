# Generated by Django 3.0.14 on 2021-04-25 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0046_auto_20210425_0828'),
        ('userprofile', '0005_auto_20210425_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemenuitem',
            name='item_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='profilemenuitem',
            name='slug',
            field=models.CharField(help_text="Must be the Item Page's slug", max_length=30),
        ),
    ]
