from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *


# sana va sonni ikki oraliq bo'yicha qidirish


class BurgerViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Burgers.objects.all().order_by('id')
    serializer_class = BurgerSerializer
    pagination_class = None

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    # @ -fts PostgreSQL o'rnatgandan keyin ishlatilsin
    search_fields = ['^name']
    ordering_fields = ['name', 'price', 'width', 'height']

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'POST', 'UPDATE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]


class CategoryViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all().order_by('order')
    serializer_class = CategorySerializer
    pagination_class = None

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'POST', 'UPDATE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'POST', 'UPDATE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]
