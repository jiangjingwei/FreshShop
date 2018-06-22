from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .filters import GoodsFilter
from .models import Goods, GoodsCategory
from .serializer import GoodsSerializer,GoodsCategorySerializer

# class GoodsListView(APIView):
#
#     def get(self, request):
#         goods = Goods.objects.all()[:10]
#         serializer = GoodsSerializer(goods, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class GoodsResultSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = 'p'
#     max_page_size = 20
#
#
# class GoodsListView(generics.ListAPIView):
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsResultSetPagination


class GoodsResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 20


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    """ 商品列表，分页，搜索，过滤，排序 """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ('=name', '^goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        list:
            商品分类数据
    """

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer


