from django.db import models

# Create your models here.

class Olts(models.Module):
    name = models.CharField(max_length=50,unique=True)
	ip = models.CharField(max_length=16,unique=True)
	upswitch = models.CharField(max_length=50,unique=True,blank=True,null=True)
	produce = models.CharField(max_length=20)
	odf = models.CharField(max_length=100)
	upports = models.CharField(max_length=100)
