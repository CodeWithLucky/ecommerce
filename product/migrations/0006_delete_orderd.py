# Generated by Django 5.0.6 on 2024-06-03 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_orderd'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orderd',
        ),
    ]