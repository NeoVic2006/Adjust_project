from rest_framework import serializers
from app.models import Sales


class SalesSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%Y-%m-%d', required=False)
    channel = serializers.CharField(max_length=255, required=False)
    country = serializers.CharField(max_length=255, required=False)
    os = serializers.CharField(max_length=255, required=False)
    impressions = serializers.IntegerField()
    clicks = serializers.IntegerField()
    installs = serializers.IntegerField()
    spend = serializers.FloatField()
    revenue = serializers.FloatField()

    class Meta:
        model = Sales
        fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')