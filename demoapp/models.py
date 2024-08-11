from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    standard = models.IntegerField()
