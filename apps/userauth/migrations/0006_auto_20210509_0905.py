# Generated by Django 3.0.14 on 2021-05-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_auto_20210509_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='N/A', max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='N/A', max_length=30, null=True, verbose_name='Last name'),
        ),
    ]