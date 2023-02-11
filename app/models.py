from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=9)
    house_number = models.PositiveIntegerField()
    street = models.CharField(max_length=30)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete= models.CASCADE)



