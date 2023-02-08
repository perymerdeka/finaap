from django.urls import path, include

urlpatterns = [
    path("api/", include("apps.bank.api.router"))

    # fungsi untuk akses web
]

