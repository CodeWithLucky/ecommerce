# Generated by Django 5.0.1 on 2024-06-03 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_gallery_image_productimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderd',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderd',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Orderd',
        ),
    ]
