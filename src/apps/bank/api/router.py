from django.urls import path
from rest_framework import routers


from apps.bank.api.views import CurrencyListAPIView

routes = routers.SimpleRouter()

urlpatterns: list = [
    path("curencies", CurrencyListAPIView.as_view(), name="currencies")
]
