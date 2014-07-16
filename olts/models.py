from django.db import models

# Create your models here.

class Olts(models.Module):
    name = models.CharField(max_length=50,unique=True)
	ip = models.IPAddressField(unique=True)
	upswitch = models.CharField(max_length=50,unique=True,blank=True,null=True)
	type = models.CharField(max_length=20)
	odf = models.CharField(max_length=100,blank=True)
    area = models.CharField(max_length=50)
	upbandwidth = models.CharField(max_length=5,blank=True)
	
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

class dataproject(models.Module):
    area = models.CharField(max_length = 20)
    olt = models.IPAddressField()
	vlantype = models.CharField(max_length=10)
    voicetype = models.CharField(max_length=10)
    pvlan_manage = models.IntegerField(blank=True)
	cvlan_manage = models.IntegerField(blank=True)
	pvlan_data_start = models.IntegerField()
	cvlan_data_start = models.IntegerField()
	pvlan_data_end = models.IntegerField()
	cvlan_data_end = models.IntegerField()
	pvlan_voice_start = models.IntegerField()
	cvlan_voice_start = models.IntegerField()
	pvlan_voice_end = models.IntegerField()
	cvlan_voice_end = models.IntegerField()
	
class numbersrc(models.Module):
    phy_10k_start = models.CharField(max_length=10)
	phy_10k_used = models.CharField(max_length=10)
	phy_10k_end = models.CharField(max_length=10)
	phy_1k_start = models.CharField(max_length=10)
	phy_1k_used = models.CharField(max_length=10)
	phy_1k_end = models.CharField(max_length=10)
	phy_1h_start = models.CharField(max_length=10)
	phy_1h_used = models.CharField(max_length=10)
	phy_1h_end = models.CharField(max_length=10)
	
