from django.urls import path
from rest_framework import routers


from apps.bank.api.views import CurrencyListAPIView, CategoryViewSet, TransactionModelViewSet

router = routers.SimpleRouter()


# register viewset
router.register(r"categories", CategoryViewSet, basename="category") # category-list
router.register(r"transactions", TransactionModelViewSet, basename="transaction")

urlpatterns: list = [
    path("curencies", CurrencyListAPIView.as_view(), name="currencies"),    

] + router.urls # <- kita daftarkan disini
