from django.db import models

# Create your models here.

class Olts(models.Module):
    name = models.CharField(max_length=50,unique=True)
	ip = models.CharField(max_length=16,unique=True)
	upswitch = models.CharField(max_length=50,unique=True,blank=True,null=True)
	
