# Generated by Django 3.0.14 on 2021-05-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userauth.SupplierUser'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.ProductUnit'),
        ),
        migrations.AddField(
            model_name='pickuppoint',
            name='managers',
            field=models.ManyToManyField(blank=True, to='userauth.ManagerUser'),
        ),
        migrations.AddField(
            model_name='pickuppoint',
            name='suppliers',
            field=models.ManyToManyField(blank=True, to='userauth.SupplierUser'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userauth.CustomerUser'),
        ),
    ]
