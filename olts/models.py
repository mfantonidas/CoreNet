from django.db import models

# Create your models here.

class Olts(models.Module):
    name = models.CharField(max_length=50,unique=True)
	ip = models.IPAddressField(unique=True)
	upswitch = models.CharField(max_length=50,unique=True,blank=True,null=True)
	type = models.CharField(max_length=20)
	odf = models.CharField(max_length=100)
<<<<<<< HEAD
	upport = models.CharField(max_length=100)
=======
	upports = models.CharField(max_length=100)
<<<<<<< HEAD
    area = models.CharField(max_length=50)
	cvlanstart_bn = models.IntegerField()
	cvlanend_bn = models.IntegerField()
	cvlanusing_bn = models.IntegerField()
	pvlan_bn = models.IntegerField()
	pvlan_bnvoice = models.IntegerField()
	pmanage = models.IntegerField()
	cmanage = models.IntegerField()
	pvlan_hstart = models.IntegerField()
	pvlan_hend = models.IntegerField()
	pvlan_useing = models.IntegerField()
	cvlan_hstart = models.IntegerField()
	cvlan_hend = models.IntegerField()
	cvlan_husing = models.IntegerField()
	cvlan_hvoice = models.IntegerField()
	
class ftto(models.Module):
    name = models.CharField(max_length=50,unique=True)
    oltip = models.IPAddressField(unique=True)
    sn = models.CharField(max_length=20,unique=True)
    obd = models.CharField(max_length=20,unique=True)
    pvlan = models.IntegerField()
    cvlan = models.IntegerField()
    ording = models.IntegerField()
    description = models.CharField(max_length = 100, blank=True)

class fttx(models.Module)
    name = models.CharField(max_length=100,unique=True)
	manage_ip = models.IPAddressField(unique=True)
	voice_ip = models.IPAddressField(unique=True)
    oltip = models.IPAddressField(unique=True)
    obd = models.CharField(max_length=20,unique=True)
    reginfo = models.CharField(max_length=50,unique=True)
    pvlan_manage = models.IntegerField()
    cvlan_manage = models.IntegerField()
    pvlan_date = models.IntegerField()
    cvlan_datastart = models.IntegerField()
    cvlan_dataend = models.IntegerField()
    pvlan_voice = models.IntegerField()
    cvlan_voice = models.IntegerField()
	pots = models.IntegerField()
    startnum = models.CharField(max_length=20,blank=True)
    endnum = models.CharField(max_length=20,blank=True)
	console = models.CharField(max_length=50,blank=True)
    
=======
>>>>>>> 799e7654dae0b8ca8a6b86676e02de228221414e
>>>>>>> e527b9dbdb813889d59d710892d4218088c651b8
