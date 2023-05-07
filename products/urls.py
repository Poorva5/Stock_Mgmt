from django.urls import include, path
from rest_framework import routers

from .views import DashboardView, OrderView

router = routers.DefaultRouter()
router.register(r"dashboard", DashboardView)
router.register(r"orders", OrderView)

urlpatterns = [
    path("", include(router.urls)),
]
