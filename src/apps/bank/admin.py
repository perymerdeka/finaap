
from django.contrib import admin

from .models import TransactionModel, CategoryModel, CurrencyModel

# Register your models here.
class TransactionModelAdmin(admin.ModelAdmin):
    pass

class CategoryModelAdmin(admin.ModelAdmin):
    pass

class CurrencyModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(TransactionModel, TransactionModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(CurrencyModel, CurrencyModelAdmin)

