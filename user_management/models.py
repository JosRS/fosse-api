from django.db import models


# Create your models here.
class UserManagement(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
    brithday = models.DateTimeField()
    profile_photo = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    vip = models.BooleanField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    frequency_purchase = models.BigIntegerField()
    notify = models.BooleanField()
    frequency_size = models.CharField(max_length=10)


class Tags(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(UserManagement, on_delete=models.CASCADE)
