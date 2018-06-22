import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):

    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gt')
    price_man = django_filters.NumberFilter(name='shop_price', lookup_expr='lt')
    # name = django_filters.CharFilter(name='name', lookup_expr='contains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_man']
