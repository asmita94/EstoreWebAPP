# Generated by Django 5.0 on 2024-01-18 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgqpp', '0015_cart_gty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('gty', models.IntegerField(default=1)),
                ('pid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, to='msgqpp.product2')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
