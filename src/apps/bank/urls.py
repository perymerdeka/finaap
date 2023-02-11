from django.urls import path, include

urlpatterns = [
    path("api/", include("apps.bank.api.routes"))

    # fungsi untuk akses web
]

