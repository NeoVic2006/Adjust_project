from rest_framework import serializers
from app.models import Stock


class StockSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%Y-%m-%d', required=False)
    channel = serializers.CharField(max_length=255, required=False)
    country = serializers.CharField(max_length=255, required=False)
    os = serializers.CharField(max_length=255, required=False)
    impressions = serializers.IntegerField()
    clicks = serializers.IntegerField()
    installs = serializers.IntegerField()
    spend = serializers.FloatField()
    revenue = serializers.FloatField()

    CPI = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Stock
        fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'CPI')