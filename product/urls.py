from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products_view, name='products'), 
    path('category/<int:category_id>/', views.products_category_view, name='products-by-category'), 
    path('contact/',views.contact_view,name="contacts"), 
    path('cart/',views.cart_view,name="cart"),
    path('checkout/',views.checkout_view,name="checkout")
    # path('category/',views,name=""),
    # path('brand/',views,name="")
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
