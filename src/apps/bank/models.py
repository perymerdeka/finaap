from django.db import models

# Create your models here.

class CurrencyModel(models.Model):
    code = models.CharField(max_length=3, unique=True, blank=True)
    name = models.CharField(max_length=32, unique=True, blank=True)

    # inisiasi bagaimana di tampilkan di django admin
    def __str__(self) -> str:
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=32, blank=True)

class TransactionModel(models.Model):
    amount = models.DecimalField(max_length=15, decimal_places=2)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.PROTECT, related_name="transactions")
    date = models.DateTimeField()
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions")

    def __str__(self) -> str:
        return f"{self.id}. {self.amount} {self.currency.code} {self.date}"