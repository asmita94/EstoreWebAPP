# Generated by Django 5.0 on 2024-01-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgqpp', '0004_product2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product2',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.IntegerField(verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Avalable'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='cate',
            field=models.IntegerField(choices=[(1, 'Mobile'), (2, 'Cloth'), (3, 'Cloth')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Avalable'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Product Name'),
        ),
    ]
