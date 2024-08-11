from django.urls import path 
from .views import CurrencyListView, CurrencyHistoryView, ConvertCurrencyView, UpdateCurrencyView

urlpatterns = [
    path("currencies/", CurrencyListView.as_view(), name="currency_list"), 
    path("history/", CurrencyHistoryView.as_view(), name="currency_history"),
    path("convert/", ConvertCurrencyView.as_view(), name="convert_currency"),
    path("update/", UpdateCurrencyView.as_view(), name="update_currency")
]