from django.db import models

# Create your models here.
from django.db import models


class Sales(models.Model):
    date = models.DateField(['%Y-%m-%d'])
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    impressions = models.IntegerField() 
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()


"""
COPY app_sales(date,channel,country,os,impressions,clicks,installs,spend,revenue) 
FROM 'C:\Adjust_project/dataset.txt' DELIMITER ','  CSV HEADER;
"""