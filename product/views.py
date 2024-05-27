from django.shortcuts import render
from . models import Product,Tag,Category,Status,SubCategory,Brand,Attribute,Attribute_Group,Currency

# Create your views here.
def index(request):
    product = Product.objects.all()
    tag = Tag.objects.all()
    category = Category.objects.all()
    status = Status.objects.all()
    sub_category = SubCategory.objects.all()
    brand = Brand.objects.all()
    attribute = Attribute.objects.all()
    attribute_group = Attribute_Group.objects.all()
    currency = Currency.objects.all()

    context = {
        'product' : product,
        'tag' : tag,
        'category' : category,
        'status' : status,
        'sub_category' : sub_category,
        'brand' : brand,
        'attribute' : attribute,
        'attribute_group' : attribute_group,
        'currency' : currency
    }
        
        
    

    return render(request, 'index.html',context)


