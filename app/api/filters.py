
from django_filters import rest_framework as rfilters
from app.models import Stock

from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from datetime import date


class StockFilter(rfilters.FilterSet):

    class Meta:
        model = Stock
        fields = ['id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue']

    date_to = rfilters.CharFilter(method='m_date_to', label='date_to')
    date_from = rfilters.CharFilter(method='m_date_from', label='date_from')
    date = rfilters.CharFilter(method='date_exact', label='date')

    def date_exact(self, queryset, name, value):
        year, month, day = self.date_split(value)
        cdate = date(year, month, day)
        return queryset.filter(date=cdate)

    def m_date_to(self, queryset, name, value):
        year, month, day = self.date_split(value)
        cdate = date(year, month, day)
        return queryset.filter(date__lte=cdate)

    def m_date_from(self, queryset, name, value):
        year, month, day = self.date_split(value)
        cdate = date(year, month, day)
        return queryset.filter(date__gte=cdate)

    def date_split(self, value):
        return [int(x) for x in value.split('-')]


    groupby = rfilters.CharFilter(method='groupby_filter', label='groupby')

    def groupby_filter(self, queryset, name, value):
        return queryset.values(*self.request.query_params.getlist('groupby')).annotate(
                                impressions=Sum('impressions'),
                                clicks=Sum('clicks'),
                                installs=Sum('installs'),
                                spend=Sum('spend'),
                                revenue=Sum('revenue'),
                                CPI=ExpressionWrapper((F('spend')/F('installs')), output_field=DecimalField())
                                )

