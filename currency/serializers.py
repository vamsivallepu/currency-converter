from rest_framework import serializers
from .models import Currency, History, ExchangeRate

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"
        # fields = ["author", "price"]

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class ExchangeRateSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    class Meta:
        model = ExchangeRate
        fields = ['currency', 'price_wrt_usd']

    
