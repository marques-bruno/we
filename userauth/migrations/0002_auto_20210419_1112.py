# Generated by Django 3.0.14 on 2021-04-19 11:12

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['last_name']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='additional_information',
            field=models.CharField(blank=True, max_length=4096, null=True, verbose_name='Additional information'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address1',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Address line 1'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address2',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Address line 2'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='profile_pics/default-user-avatar.png', upload_to='profile_pics/', verbose_name='Profile Picture'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Postal Code'),
        ),
    ]
