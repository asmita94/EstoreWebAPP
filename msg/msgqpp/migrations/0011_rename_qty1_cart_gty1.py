# Generated by Django 5.0 on 2024-01-17 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgqpp', '0010_remove_cart_qty_cart_qty1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='qty1',
            new_name='gty1',
        ),
    ]
