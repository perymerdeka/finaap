from django.urls import path
from rest_framework import routers


from apps.bank.api.views import CurrencyModelViewSet, TransactionModelViewSet, CategoryModelViewSet

router = routers.SimpleRouter()


# register viewset
router.register(r"categories", CategoryModelViewSet, basename="category") # category-list
router.register(r"transactions", TransactionModelViewSet, basename="transaction")
router.register(r"currencies", CurrencyModelViewSet, basename="currency")

urlpatterns: list = [   

] + router.urls # <- kita daftarkan disini
