from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('products/',views,name=""),
    # path('category/',views,name=""),
    # path('brand/',views,name="")
]
