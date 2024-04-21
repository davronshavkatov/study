from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from .models import *
from .serializers import *


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = OrdersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if 'order_details' in data and isinstance(data['order_details'], list):
                order_details = data['order_details']
                order = serializer.data['id']
                for order_detail in order_details:
                    order_detail['order'] = order
                detail_serializer = OrderDetailSerializer(data=order_details, many=True)
                if detail_serializer.is_valid():
                    detail_serializer.save()
                    data = serializer.data
                    data['order_details'] = detail_serializer.data
                    return Response(data, status=status.HTTP_201_CREATED)
                else:
                    return Response(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            serializer = OrderDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = OrderDetailSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
