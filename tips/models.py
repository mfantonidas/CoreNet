from django.db import models

# Create your models here.

class contact_info(models.Model):
    department = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
	duty = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.department
