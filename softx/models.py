from django.db import models

# Create your models here.

class corenet_ne(models.Model):
    name = models.CharField(max_length=50,unique=True)
    ipaddr = models.IPAddressField(unique=True)
    netype = models.CharField(max_length=20,unique=True)
    snmpaddr = models.IPAddressField(blank = True)
    uplink = models.CharField(max_length=50,blank=True)
	
class softxinfo(models.Model):
    area = models.CharField(max_length=20,unique=True)
	
class IMSinfo(models.Model):
    area = models.CharField(max_length=20,unique=True)
