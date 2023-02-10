from django.urls import path
from rest_framework import routers


from apps.bank.api.views import CurrencyListAPIView, TransactionListAPIView, CategoryListAPIView

routes = routers.SimpleRouter()

urlpatterns: list = [
    path("curencies", CurrencyListAPIView.as_view(), name="currencies"),
    path("categories", CategoryListAPIView.as_view(), name="categories"),
    path("transactions", TransactionListAPIView.as_view(), name="transactions"),

]
