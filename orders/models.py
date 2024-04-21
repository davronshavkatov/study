import uuid

from django.db import models
from product.models import Burgers
from account.models import User


class Orders(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0)
    DELIVERY_TYPE = (
        ("dostavka", "dostavka"),
        ("samovizov", "samovizov")
    )
    PAYMENT_TYPE = (
        ("click", "click"),
        ("payme", "payme"),
        ("nalichniy", "nalichniy")
    )
    delivery = models.CharField(max_length=20, choices=DELIVERY_TYPE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    address = models.CharField(max_length=300, null=True)
    kvartal = models.CharField(max_length=30, null=True, blank=True)
    dom = models.CharField(max_length=30, null=True, blank=True)
    kvartira = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    filial = models.ForeignKey("Filial", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id} {self.user}"


class OrderDetail(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    product = models.ForeignKey(Burgers, on_delete=models.CASCADE)
    price = models.FloatField()
    number = models.IntegerField(default=1)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_details")

    def __str__(self):
        return f"{self.product} {self.number}"


class Filial(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20)
    work_time = models.CharField(max_length=100, default="")


    def __str__(self):
        return f"{self.name}"