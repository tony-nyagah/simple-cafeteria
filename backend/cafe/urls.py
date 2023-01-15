from django.urls import include, path
from rest_framework import routers

from .views import CustomerViewSet, FoodItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"food-items", FoodItemViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
