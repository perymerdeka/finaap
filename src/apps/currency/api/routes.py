from .views import CurrencyScraperViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# register viewset
router.register(r"scrapers", CurrencyScraperViewSet, basename="scraper") # category-list

urlpatterns: list =  router.urls # <- kita daftarkan disini