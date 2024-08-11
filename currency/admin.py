from django.contrib import admin
from .models import Currency, History, ExchangeRate

# Register your models here.
admin.site.register(Currency)
admin.site.register(History)
admin.site.register(ExchangeRate)