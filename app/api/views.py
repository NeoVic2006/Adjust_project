from rest_framework.generics import ListAPIView
from app.models import Sales
from .serializers import SalesSerializer
from .filters import SalesFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class SalesListAPIView(ListAPIView):

    serializer_class = SalesSerializer
    queryset = Sales.objects.all()

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    filter_class = SalesFilter

    fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')

    filter_fields = fields
    search_fields = fields



