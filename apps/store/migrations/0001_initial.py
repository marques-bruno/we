# Generated by Django 3.0.14 on 2021-05-04 10:48

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PickupPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAllergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_name', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('icon', models.CharField(blank=True, max_length=512)),
            ],
            options={
                'verbose_name': 'Product Allergen',
                'verbose_name_plural': 'Product Allergens',
            },
        ),
        migrations.CreateModel(
            name='ProductLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_name', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('icon', models.CharField(blank=True, max_length=512)),
            ],
            options={
                'verbose_name': 'Product Label',
                'verbose_name_plural': 'Product Labels',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_name', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('icon', models.CharField(blank=True, max_length=512)),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('short_name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Product Unit',
                'verbose_name_plural': 'Product Units',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('price', models.FloatField(default=9999.99)),
                ('quantity', models.IntegerField(default=0)),
                ('quantity_per_unit', models.FloatField(default=1)),
                ('description', wagtail.core.fields.RichTextField(blank=True, default='Fresh, local, fair price.', null=True)),
                ('farmers_advice', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('allergens', models.ManyToManyField(blank=True, to='store.ProductAllergen')),
                ('labels', models.ManyToManyField(blank=True, to='store.ProductLabel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
