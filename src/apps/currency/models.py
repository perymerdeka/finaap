from django.db import models

# Create your models here.

class CurrencyScraperModel(models.Model):
    code = models.CharField(max_length=5)
    alphaCode = models.CharField(max_length=5)
    numericCode = models.IntegerField()
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=16)
    date = models.DateField()
    inverseRate = models.DecimalField(max_digits=16)

    def __str__(self) -> str:
        return self.name



