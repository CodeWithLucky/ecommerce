from django.shortcuts import render,get_object_or_404
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
    recommend_products = Product.objects.order_by('-views')[:3]



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
        'recommend_products' : recommend_products
    }
        

    return render(request, 'index.html',context)

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category, Brand

def products_view(request):
    # Retrieve all products initially
    products = Product.objects.all()

    # Retrieve categories, subcategories, and manufacturers
    categories = Category.objects.all()
    sub_categories = Category.objects.prefetch_related('subcategories').all()
    sub_cat = SubCategory.objects.all()
    manufacturers = Brand.objects.all()
    
    product_ids = request.POST.get('category_id')
    print("This is id:", product_ids)

    if product_ids:
        try:
            # Convert product_ids to an integer
            product_ids = int(product_ids)
            # Filter products based on the selected category
            products = Product.objects.filter(SubCategory__parent_category_id=product_ids)
            
        except ValueError:
            print("Invalid category ID")
            pass
    

    # if product_ids:
    #     try:
    #         product_ids = int(product_ids)
    #         filtered_products = Product.objects.filter(SubCategory__parent_category_id = product_ids)
    #         print (products)
    #     except (ValueError, Category.DoesNotExist):
    #     # Handle invalid input or category not found
    #         filtered_products = products
    # else:
    #     filtered_products = products

        



    # Get search query from request
    search = request.GET.get('search')
    if search:
        products = products.filter(title__icontains=search)

    # Paginate the products after filtering
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')

    # If search query exists, default to the first page of search results
    if search:
        page_number = 1

    page_products = paginator.get_page(page_number)

    context = {
        'products': page_products,
        'product-list' : product_ids,
        'categories': categories,
        'sub_categories': sub_categories,
        'sub_cat': sub_cat,
        'manufacturer': manufacturers,
        'product_sort' : products,
    }

    return render(request, 'products.html', context)




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

def products_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Increment the view count
    product.views += 1
    product.save()
    
    context = {
        'product': product,
    }
    
    return render(request, 'product_detail.html', context)

def contact_view(request):
    return render(request, 'contact.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')






# def products_view(request):
#     product = Product.objects.all()
#     recommended_products = products_recommend(request)


#     context = {
#         'products': product,
#         'recommended_products': recommended_products,
        
#     }
#     return render (request,'products.html')


