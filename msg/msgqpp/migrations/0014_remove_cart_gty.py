# Generated by Django 5.0 on 2024-01-17 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgqpp', '0013_rename_qty_cart_gty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='gty',
        ),
    ]