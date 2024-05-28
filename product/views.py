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
    latest_products = Product.objects.order_by('-added_at')[:4]
    price_order = Product.objects.order_by('-new_price')
    

    context = {
        'product' : product,
        'tag' : tag,
        'categories' : category,
        'status' : status,
        'sub_category' : sub_category,
        'brand' : brand,
        'attribute' : attribute,
        'attribute_group' : attribute_group,
        'currency' : currency,
        'latest_products' : latest_products,
    }
        
    for product in price_order:
        print(product.new_price)

    return render(request, 'index.html',context)

def products_view(request):
    #sort_by=request.Get.get('sort_by','price')
    products = Product.objects.all()
    category = Category.objects.all()
    sub_categories = Category.objects.prefetch_related('subcategories').all()
    # if sort_by=='price_high_to_low':
    #     products=products.order_by('price')
    # elif sort_by=='price_low_to_high':
    #     products=products.order_by('price')
    

    context = {
        'products' : products,
        'categories' : category,
        'sub_categories' : sub_categories,
        # 'sort_by':sort_by
    }

    return render(request, 'products.html',context)



def products_category_view(request):
    categories = Category.objects.all()
    category_products = {}

    for category in categories:
        subcategories = category.subcategory_set.all()
        products = Product.objects.filter(SubCategory__in=subcategories).order_by('-added_at')
        category_products[category] = products

    context = {
        'category_products': category_products
    }

    return render(request, 'products_by_category.html', context)
    
def contact_view(request):
    return render(request, 'contact.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

