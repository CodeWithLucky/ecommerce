from django.contrib import admin
from . models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title'
        ]
    

    

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'parent_category',
        'title',
        'images',
        'description', 
        'status'
    ]
    

class StatusAdmin(admin.ModelAdmin):
    list_display = [
        'status'
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]

class CurencyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'rate',
        'status',
        'symbol'
    ]


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'brand_name',
        'status'
    ]

class SliderAdmin(admin.ModelAdmin):
    list_display = [
        'images',
        'alt_text',
        'link',
        'caption',
        'sort_by'
    ]


class Attribute_Group_Admin(admin.ModelAdmin):
    list_display = [
        'title',
        'status'
    ]

class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        'attribute_group_id',
        'title',
        'status'
    ]

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = [
        'SubCategory',
        'brand',
        'tag',
        'title',
        'new_price',
        'image',
        'quantity',
        'slug'
    ]


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Attribute_Group, Attribute_Group_Admin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Currency, CurencyAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)