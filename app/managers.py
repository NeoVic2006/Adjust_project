from django.db import models
from .models import *
from django.db.models import F, ExpressionWrapper, DecimalField


class StockQuerySet(models.QuerySet):
    def calculated_CLI(self):
        return self.model.objects.annotate(CPI=ExpressionWrapper((F('spend')/F('installs')),output_field=DecimalField()))


class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)

    def calculated_CLI(self):
        return self.get_queryset().calculated_CLI()