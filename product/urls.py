from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products_view, name='products'), 
    path('products_detail/<int:product_id>/', views.products_detail, name='products_detail'), 
    path('products-by-category/', views.products_category_view, name='products_by_category'),
    path('products/ajax/',views.products_by_bar,name="products-by-bar"),
    path('contact/',views.contact_view,name="contacts"), 
    path('cart/',views.cart_view,name="cart"),
    path('checkout/',views.checkout_view,name="checkout"),
    # path('category/',views,name=""),
    # path('brand/',views,name="")
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
