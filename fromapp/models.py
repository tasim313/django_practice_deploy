from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    ipaddress = models.GenericIPAddressField()
    contact = models.CharField(max_length=100)
