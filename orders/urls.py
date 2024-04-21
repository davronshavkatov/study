from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("order", OrdersViewSet)
router.register("order_detail", OrderDetailViewSet)
router.register("filial", FilialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
