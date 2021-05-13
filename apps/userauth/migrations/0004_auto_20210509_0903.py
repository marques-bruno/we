# Generated by Django 3.0.14 on 2021-05-09 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20210509_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='additional_information',
            field=models.CharField(blank=True, default='N/A', max_length=4096, null=True, verbose_name='Additional information'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.CharField(blank=True, default='N/A', max_length=250, null=True, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, default='N/A', max_length=250, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, default='N/A', max_length=150, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='first_name',
            field=models.CharField(blank=True, default='N/A', max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_primary',
            field=models.BooleanField(blank=True, default='False', null=True, verbose_name='Primary address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='last_name',
            field=models.CharField(blank=True, default='N/A', max_length=30, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='mobile_phone',
            field=models.CharField(blank=True, default='+421 000 000 000', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(blank=True, default='+421 000 000 000', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(blank=True, default='N/A', max_length=12, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=150, verbose_name='last name'),
            preserve_default=False,
        ),
    ]
