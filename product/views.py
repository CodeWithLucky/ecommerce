from django.shortcuts import render
from django.http import Http404
from . models import Product,Tag,Category,Status,SubCategory,Brand,Attribute,Attribute_Group,Currency
from . filters import ProductFilter
from django.core.paginator import Paginator

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
    latest_products = Product.objects.order_by('-added_at')[:5]
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
    product = Product.objects.all()


    category = Category.objects.all()
    sub_categories = Category.objects.prefetch_related('subcategories').all()
    # if sort_by=='price_high_to_low':
    #     products=products.order_by('price')
    # elif sort_by=='price_low_to_high':
    #     products=products.order_by('price')
    manufacturer = Brand.objects.all()

    # category_search = request.GET.get('')

    p = Paginator(product, 18)

    page = request.GET.get('page')

    page_product = p.get_page(page)
    


    search = request.GET.get('search')

    if search:
        page_product = product.filter(title__icontains = search)



        

    # product_search = ProductFilter(request.GET, queryset=Product.objects.all())
    

    context = {
        'products' : page_product,
        'categories' : category,
        'sub_categories' : sub_categories,
        'manufacturer' : manufacturer,
        # 'sort_by':sort_by
    }

    return render(request, 'products.html',context)



def products_category_view(request):
    product = Product.objects.all()
    category = Category.objects.all()
    sub_categories = Category.objects.prefetch_related('subcategories').all()
    # if sort_by=='price_high_to_low':
    #     products=products.order_by('price')
    # elif sort_by=='price_low_to_high':
    #     products=products.order_by('price')
    manufacturer = Brand.objects.all()

    category_search = request.GET.get('')

    
    search = request.GET.get('search')

    if search:
        product = product.filter(title__icontains = search)

    # product_search = ProductFilter(request.GET, queryset=Product.objects.all())
    

    context = {
        'products' : product,
        'categories' : category,
        'sub_categories' : sub_categories,
        'manufacturer' : manufacturer,
        # 'sort_by':sort_by
    }
    # categories = Category.objects.all()
    # category_products = {}

    # for category in categories:
    #     subcategories = category.subcategories.all()
    #     products = Product.objects.filter(subcategory__in=subcategories).order_by('-added_at')
    #     category_products[category] = products

    # context = {
    #     'category_products': category_products
    # }

    return render(request, 'products_by_category.html')

def products_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    
    context = {
        'products' : product,
    }

    return render(request, 'product_detail.html',context)

def contact_view(request):
    return render(request, 'contact.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

