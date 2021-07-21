from django.db import models
from .models import *


class SalesManager(models.Manager):
    def get_queryset(self):
        return self.model
