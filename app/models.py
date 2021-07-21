from django.db import models

# Create your models here.
from app.managers import StockQuerySet

class Stock(models.Model):
    date = models.DateField(['%Y-%m-%d'])
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    impressions = models.IntegerField() 
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    
    objects = StockQuerySet.as_manager()
