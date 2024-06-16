from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from .validators import validate_image_format
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to='category_images', max_length=500, null=True, blank=True, validators=[validate_image_format])
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

class Slider(models.Model):
    images = models.ImageField(upload_to='slider_image/', max_length=500, null=True, blank=True, validators=[validate_image_format])
    alt_text = models.CharField(max_length=125)
    link = models.URLField(max_length=200)
    caption = models.CharField(max_length=200)
    rank = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand_name

class Attribute_Group(models.Model):
    title = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Attribute(models.Model):
    attribute_group_id = models.ForeignKey(Attribute_Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Currency(models.Model):
    title = models.CharField(max_length=50)
    rate = models.CharField(max_length=10)
    symbol = models.CharField(max_length=4)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

class Product(models.Model):
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    new_price = models.FloatField()
    old_price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_image/', max_length=500, null=True, blank=True, validators=[validate_image_format]),
    short_description = models.TextField()
    long_description = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    attribute = models.ManyToManyField(Attribute, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

class ProductImage(models.Model):
    images = models.ImageField(upload_to='Gallery', null = True, blank= True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Maintenance(models.Model):
    is_under_maintenance = models.BooleanField(default=False)

    def __str__(self):
        return "Site Under Maintenance" if self.is_under_maintenance else "Site Operational"
    

class History(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    



