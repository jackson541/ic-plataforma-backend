from django.db import models
from django.contrib.auth.models import User
from .utils.paths import *

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to=upload_photo_user)
    address = models.TextField()

class Salesman(Person):
    town_hall_number = models.PositiveIntegerField()

class Client(Person):
    pass

class Product(models.Model):
    amount = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField()
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_photo_user)
    price = models.DecimalField(decimal_places = 2, max_digits = 3)

