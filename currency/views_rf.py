from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Currency, History, ExchangeRate
from .serializers import CurrencySerializer, HistorySerializer, ExchangeRateSerializer

class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyHistoryView(generics.ListAPIView):
    serializer_class = HistorySerializer
    def get_queryset(self):
        currency_name = self.request.query_params.get('currency_name', '')
        if currency_name:
            currency = get_object_or_404(Currency, name=currency_name)
            return History.objects.filter(currency=currency)
        return History.objects.none()

class ConvertCurrencyView(APIView):
    def get(self, request):
        from_currency = request.query_params.get('from_currency')
        to_currency = request.query_params.get('to_currency')
        amount = float(request.query_params.get('amount', 0))

        if not all([from_currency, to_currency, amount]):
            return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

        from_rate = get_object_or_404(ExchangeRate, currency__name=from_currency).price_wrt_usd
        to_rate = get_object_or_404(ExchangeRate, currency__name=to_currency).price_wrt_usd
        
        converted_amount = (amount / float(from_rate)) * float(to_rate)
        return Response({"converted_amount": converted_amount})

class UpdateCurrencyView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    lookup_field = 'currency__name'

    def get_object(self):
        currency_name = self.request.data.get('currency_name')
        return get_object_or_404(self.get_queryset(), currency__name=currency_name)

    def put(self, request, *args, **kwargs):
        currency_name = request.data.get('currency_name')
        new_value = request.data.get('new_value')

        new_value = float(new_value)

        request.data['price_wrt_usd'] = new_value
        response = self.update(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            currency = self.get_object().currency
            History.objects.create(currency=currency, price_wrt_usd=new_value)

        return response