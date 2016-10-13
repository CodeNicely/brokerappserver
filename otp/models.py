from __future__ import unicode_literals

from django.db import models

class otp_data(models.Model):
	id=models.AutoField(primary_key=True)
	mobile=models.DecimalField(max_digits=10,default=0,decimal_places=0)
	otp=models.SmallIntegerField(default=0)
	flag=models.SmallIntegerField(default=0)

class user_token_data(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True,default=0)
    access_token=models.CharField(max_length=120,blank=True,null=True)
