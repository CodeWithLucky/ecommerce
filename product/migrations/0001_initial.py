# Generated by Django 5.0.6 on 2024-05-30 05:31

import django.db.models.deletion
import django.utils.timezone
import product.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('attribute_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attribute_group')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, max_length=500, null=True, upload_to='slider_image/', validators=[product.validators.validate_image_format])),
                ('alt_text', models.CharField(max_length=125)),
                ('link', models.URLField()),
                ('caption', models.CharField(max_length=200)),
                ('rank', models.CharField(max_length=50)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rate', models.CharField(max_length=10)),
                ('symbol', models.CharField(max_length=4)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status')),
            ],
        ),
        migrations.AddField(
            model_name='attribute_group',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('images', models.ImageField(blank=True, max_length=500, null=True, upload_to='category_images', validators=[product.validators.validate_image_format])),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='product_image/', validators=[product.validators.validate_image_format])),
                ('short_description', models.TextField()),
                ('long_description', models.TextField()),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.PositiveIntegerField(default=0)),
                ('attribute', models.ManyToManyField(blank=True, to='product.attribute')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tag')),
            ],
        ),
    ]
