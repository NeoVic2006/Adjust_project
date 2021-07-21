from rest_framework.generics import ListAPIView
from app.models import Stock
from .serializers import StockSerializer
from .filters import StockFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class StockListAPIView(ListAPIView):

    serializer_class = StockSerializer
    queryset = Stock.objects.calculated_CLI()

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    filter_class = StockFilter

    fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'CPI')

    filter_fields = fields
    search_fields = fields

