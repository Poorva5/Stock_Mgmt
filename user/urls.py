from django.urls import include, path
from rest_framework import routers
from .views import AddressView

router = routers.DefaultRouter()
router.register(r'address', AddressView, basename='create-address')

urlpatterns = [
    path('', include(router.urls)),
]