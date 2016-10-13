from django.contrib import admin
from .models import *

class version_dataAdmin(admin.ModelAdmin):
	list_display=["version_id","version_no","compulsory_update"]

admin.site.register(version_data, version_dataAdmin)

# Register your models here.
