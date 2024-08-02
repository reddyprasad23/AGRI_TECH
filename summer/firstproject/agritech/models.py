from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
	farmer=models.BooleanField(default=False)
	buyer=models.BooleanField(default=False)

class FarmerTable(models.Model):
	village=models.CharField(max_length=100)
	district=models.CharField(max_length=50)
	state=models.CharField(max_length=30)
	mobile=models.IntegerField()
	land=models.IntegerField()
	crops=models.CharField(max_length=200)
	price=models.CharField(max_length=500)
	image=models.ImageField()
	usd = models.OneToOneField(User,on_delete = models.CASCADE)

class ConsumerTable(models.Model):
	phonenumber = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	idproof = models.CharField(max_length=100)
	requiredproduct = models.CharField(max_length=100)
	quantity = models.CharField(max_length=100)
	image=models.ImageField()
	usc = models.OneToOneField(User,on_delete = models.CASCADE)

class OrdersTable(models.Model):
	buyername=models.CharField(max_length=50)
	cropname=models.CharField(max_length=20)
	requantity=models.CharField(max_length=20)
	advanceamount=models.IntegerField()
	uso = models.OneToOneField(User,on_delete = models.CASCADE)
