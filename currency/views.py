from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse
from .serializers import CurrencySerializer, ExchangeRateSerializer, HistorySerializer
from .models import Currency, ExchangeRate, History
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from django.shortcuts import render


# Create your views here.
class CurrencyListView(View):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        # return HttpResponse(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'currency_list.html', {'currencies':serializer.data})

class CurrencyHistoryView(View):
    def get(self, request):
        return render(request, 'currency_history.html')

    def post(self, request):
        currency_name = request.POST.get('currency_name')
        # print("--------------------------")
        # print(currency_name)
        if currency_name!="":
            currency_required = get_object_or_404(Currency, name=currency_name)
            history = History.objects.filter(currency=currency_required)
            # history = get_object_or_404(History, currency__name=currency_name)
        else:
            return HttpResponse("Enter Proper name")
        
        serializer = HistorySerializer(history, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'currency_history.html', {'history':serializer.data})

    # def get(self, request):
    #     return render(request, 'history.html')
    
    # def post(self, request):
    #     currency_name = request.POST.get('currency_name')
    #     if currency_name!="":
    #         currency_required = Currency.objects.filter(name=currency_name)
    #         # print("---------------------")
    #         print(currency_required.first())
    #         history = History.objects.filter(currency=currency_required.first())
    #     else:
    #         return HttpResponse("Enter Proper name")
        
    #     serializer = HistorySerializer(history, many=True)
    #     return JsonResponse(serializer.data, safe=False)
        # return HttpResponse("test")

class ConvertCurrencyView(View):
    def get(self, request):
        return render(request, 'convert_currency.html')
    def post(self, request):
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))

        from_rate = get_object_or_404(ExchangeRate, currency__name=from_currency).price_wrt_usd
        to_rate = get_object_or_404(ExchangeRate, currency__name=to_currency).price_wrt_usd

        converted_amount = (amount/float(from_rate))*float(to_rate)


        # return JsonResponse({"converted_amount": converted_amount})
        return render(request, 'convert_currency.html', {'converted_amount':converted_amount})
    
class UpdateCurrencyView(View):
    def get(self, request):
        return render(request, 'update.html')
    def post(self, request):
        currency_name = request.POST.get("currency_name")
        new_value = request.POST.get("new_value")

        # request_rest = Request(request, parsers=[JSONParser()])
        # print(request_rest.data)
        currency_fk = get_object_or_404(Currency, name=currency_name)
        new_value = float(new_value)

        new_data = {
            "currency" : {
                "name" : currency_fk.name,
                "description" : currency_fk.description
            },
            "price_wrt_usd" : new_value
        }

        serializer = ExchangeRateSerializer(data=new_data)
        if serializer.is_valid():
            # print("VALIDATED")
            exchange_rate = ExchangeRate.objects.get(currency=currency_fk)
            exchange_rate.price_wrt_usd = new_value
            exchange_rate.save()

            History.objects.create(currency=currency_fk, price_wrt_usd=new_value)
            return render(request, 'update.html', {'success':True})
        else:

            return render(request, 'update.html', {'error':"Please enter valid data"})
    
    