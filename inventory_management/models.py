from django.db import models


# Create your models here.
class Inventory(models.Model):
    date = models.DateTimeField()


class Type(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    name = models.CharField(max_length=50)
    count = models.BigIntegerField()
    type = models.CharField(max_length=50)
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.DO_NOTHING)


