# Generated by Django 3.0.14 on 2021-05-06 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('userprofile', '0003_auto_20210506_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='favoritefarmerspage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='messageboardpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='pastorderspage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='pendingorderspage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='AccountInfoPage',
        ),
        migrations.DeleteModel(
            name='DashboardPage',
        ),
        migrations.DeleteModel(
            name='FavoriteFarmersPage',
        ),
        migrations.DeleteModel(
            name='MessageBoardPage',
        ),
        migrations.DeleteModel(
            name='PastOrdersPage',
        ),
        migrations.DeleteModel(
            name='PendingOrdersPage',
        ),
    ]