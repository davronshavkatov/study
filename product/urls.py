from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("burgers", BurgerViewSet)
router.register("categories", CategoryViewSet)
router.register("settings", SettingsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
