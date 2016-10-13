from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import *

def ver_check(request):
	try:
		version_row=version_data.objects.get(ver_type='arp')
		response_json={}
		response_json["success"]=True
		response_json["version_no"]=version_row.version_no
		response_json["compulsory_update"]=version_row.compulsory_update

	except:
		response_json["success"]=False
		response_json["message"]="version_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))



# Create your views here.
