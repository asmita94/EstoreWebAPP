# Generated by Django 5.0 on 2024-01-17 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgqpp', '0011_rename_qty1_cart_gty1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='gty1',
            new_name='qty',
        ),
    ]
