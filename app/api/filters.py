
from django_filters import rest_framework as rfilters
from app.models import Sales

from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from datetime import date


class SalesFilter(rfilters.FilterSet):

    class Meta:
        model = Sales
        fields = ['id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue']

    groupby = rfilters.CharFilter(method='groupby_filter', label='groupby')


    def groupby_filter(self, queryset, name, value):
        return queryset.values(*self.request.query_params.getlist('groupby')).annotate(
                                impressions=Sum('impressions'),
                                clicks=Sum('clicks'),
                                installs=Sum('installs'),
                                spend=Sum('spend'),
                                revenue=Sum('revenue')
                            )
