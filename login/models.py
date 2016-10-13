from __future__ import unicode_literals

from django.db import models

class user_data(models.Model):
	name= models.CharField(max_length=120, blank=True, null=True)
	user_id= models.AutoField(primary_key=True)
	mob=models.SmallIntegerField(max_digits=10 , default=0)
	firm=models.CharField(max_length=120, blank=True, null=True)
	

# Create your models here.
