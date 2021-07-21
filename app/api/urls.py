from django.urls import path
from .views import StockListAPIView


urlpatterns = [
path('api/stock', StockListAPIView.as_view())
]