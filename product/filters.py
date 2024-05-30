from . models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product  # Use an equal sign here instead of a colon
        fields = {
            'title': ['icontains'],  # The field name should be enclosed in quotes and specified as a dictionary
        }

