from rest_framework import serializers

from .models import *


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filial
        fields = '__all__'