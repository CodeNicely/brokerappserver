from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def send_otp(request):
	try:
		url='http://api.msg91.com/api/sendhttp.php?authkey=125195AvX4LUlVf57dcd941&mobiles='
		mobile=str(request.POST.get("mobile"))
		#mobile=str(9406277619)
		n=random.randint(1000,9999)
		url+=str(mobile)
		otp=str(n)

		url+='&message='+' \nVerification code for the app is '+otp
		url+='&sender=mARPIT&route=4'
	
		result = requests.request('GET', url)

		try:
			otp_list=otp_data.objects.get(mobile=mobile)
			setattr(otp_list,'otp',int(otp))
			otp_list.save()
		except:
			otp_data.objects.create(mobile=mobile,otp=int(otp))
		response_json={"success":True,"message":"otp sent"}
	except:
		response_json={"success":False,"message":"otp not sent"}
	print str(response_json)
	return HttpResponse(str(response_json))
#@csrf_exempt
@csrf_exempt
def ver_otp(request):
	try:
		name=str(request.POST.get("name"))
		mobile=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))
		company_name=str(request.POST.get("firm"))
		#mobile=str(9406277619)

		print "get method successful"
		print"\n"
		access_token_str=str(random.randint(1000,9999))+mobile+str(random.randint(1000,9999))
		#otp=7541
		otp_list=otp_data.objects.get(mobile=mobile)
		if otp_list.otp== int(otp):
			setattr(otp_list,'flag',int(1))
			otp_list.save()
			try:
				user_list=user_data.objects.get(mobile=mobile)
				setattr(user_list,'name',name)
				setattr(user_list,'company_name',company_name)
				setattr(user_list,'mobile',mobile)
				user_list.save()

				access_token_str=str(user_token_data_list.access_token)
				response_json={
				"success":True,
				"message":"successful",
				"access_token":access_token_str,}

			except:
				try:
					user_data.objects.create(
						name=name,
						company_name=company_name,
						mobile=mobile,
						#access_token=access_token
						)
					user_list=user_data.objects.get(mobile=mobile)
					user_token_data.objects.create(
						id=user_list.id,
						access_token=access_token_str)
					response_json={
					"success":True,
					"message":"successful",
					"access_token":access_token_str,
					}
				except:
					response_json={
					"success":False,
					"access_token":access_token_str,
					}

		else:
			response_json={
			"success":False,
			"message":"not verified otp did not match",
			"access_token":"NULL",
			}

	except:
		response_json={
			"success":False,
			"message":"number does not exsist",
			"access_token":"NULL",
			}
	print str(response_json)
	return HttpResponse(str(response_json))