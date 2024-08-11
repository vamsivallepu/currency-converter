from django.db import models
from django.utils import timezone

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class History(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price_wrt_usd = models.DecimalField(max_digits=10, decimal_places=5)
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.currency.name+" last update at : "+str(self.date_recorded)
    

class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price_wrt_usd = models.DecimalField(max_digits=10, decimal_places=5)
    last_updated =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.currency.name
