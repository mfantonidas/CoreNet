from django.db import models

# Create your models here.

class corenet_ne(models.Model):
    name = models.CharField(max_length=50,unique=True)
    ipaddr = models.IPAddressField(unique=True)
    netype = models.CharField(max_length=20)
    logaddr = models.IPAddressField(blank = True)
    uplink = models.CharField(max_length=50,blank=True)
	logname = models.CharField(max_length=50, blank=True)
	logpass = models.PasswordField(max_length=50，blank=True)
	
class softxinfo(models.Model):
    locate = models.CharField(max_length=5)
    area = models.CharField(max_length=20,unique=True)
    localaddr = models.IPAddressField()
    residue_fccus = models.CharField(max_length=100)
    lp = models.IntegerField()
    rchs = models.IntegerField()
    csc = models.IntegerField()
		
class IMSinfo(models.Model):
    area = models.CharField(max_length=20,unique=True)
    imssub_action = models.CharField(max_length=10)
    imssub_ac = models.IntegerField()
    imssub_nc = models.CharField(max_length=5)
    imssub_domain = models.CharField(max_length = 20)
    imssub_usertype = models.IntegerField()
    imssub_imputplid = models.IntegerField()
    imssub_sptplid = models.IntegerField()
    imssub_chargtplid = models.IntegerField()
    imssub_captplid = models.IntegerField()
    NAPTRRecord_zonename = models.CharField(max_length = 50)
    NAPTRRecord_order = models.IntegerField()
    NAPTRRecord_preference = models.IntegerField()
    NAPTRRecord_flags = models.CharField(max_length=5)
    NAPTRRecord_service = models.CharField(max_length=20)
    NAPTRRecord_replacement = models.CharField(max_length=5)
    NAPTRRecord_ttl = models.IntegerField()
    MGWAGCF_gwtp = models.IntegerField()
    MGWAGCF_ptype = models.IntegerField()
    MGWAGCF_la = models.IPAddressField()
    MGWAGCF_pa = models.IPAddressField()
    MGWAGCF_masteragcf = models.CharField(max_length=10)
    MGWAGCF_slaveragcf = models.CharField(max_length=10)
    ASBRAGCF_regtp = models.IntegerField()
    ASBRAGCF_netid = models.CharField(max_length=10)
    ASBRAGCF_netinfo = models.CharField(max_length=10)
    ASBRAGCF_phncon = models.CharField(max_length=10)
    ASBRAGCF_digmap = models.IntegerField(max_length=5)
    ASBRAGCF_emgcn = models.CharField(max_length=10)
    SBR_nc = models.CharField(max_length=5)
    SBR_domain = models.CharField(max_length=20)
    SBR_lp = models.IntegerField()
    SBR_csc = models.IntegerField()
