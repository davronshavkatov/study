import uuid
from django.db import models


class Burgers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True,  blank=True)
    definition_uz = models.TextField(null=True, blank=True)
    definition_en = models.TextField(null=True, blank=True)
    definition_ru = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='burgers', default='burgers\empty_cart.png', null=True)
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name="burgers")

    def __str__(self):
        return str(self.name_ru)


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name_ru)


class Settings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

