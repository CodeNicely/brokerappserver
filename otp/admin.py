from django.contrib import admin
from .models import *

class otp_dataAdmin(admin.ModelAdmin):
	list_display=["id","otp","flag"]

admin.site.register(otp_data, otp_dataAdmin)
# Register your models here.
