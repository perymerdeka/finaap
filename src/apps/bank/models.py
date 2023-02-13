from django.db import models

# Create your models here.

class CurrencyModel(models.Model):
    code = models.CharField(max_length=3, unique=True, blank=True, null=True)
    name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "currency"

    # inisiasi bagaimana di tampilkan di django admin
    def __str__(self) -> str:
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name = "categorie"

    def __str__(self) -> str:
        return self.name


class TransactionModel(models.Model):
    amount = models.DecimalField(max_length=15, decimal_places=2, max_digits=8)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.PROTECT, related_name="transactions")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions")

    class Meta:
        verbose_name = "transaction"
       
       
    def __str__(self) -> str:
        return f"{self.id}. {self.amount} {self.currency.code}"