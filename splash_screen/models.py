from __future__ import unicode_literals

from django.db import models

class version_data(models.Model):
	version_id= models.AutoField(primary_key=True)
	version_no=models.SmallIntegerField(default=0)
	compulsory_update=models.SmallIntegerField(default=0)
	ver_type=models.CharField(max_length=120, blank=True,null=True)



# Create your models here.
