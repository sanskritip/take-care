from django.shortcuts import render
import json
from .models import OauthCreds
# Create your views here.
from googleapiclient.discovery import build
from django.shortcuts import render,redirect
from datetime import datetime
import time
import google.oauth2.credentials
import google_auth_oauthlib.flow
import httplib2
import google_auth_httplib2
# Create your views here.

def logout_google(request):
	for i in OauthCreds.objects.all():
		if i.user == request.user:
			i.delete()
			break
	return redirect('auth_display')

def calc_step(data):
	steps = 0
	for i in data['point']:
		steps+=int(i['value'][0]['intVal'])
	return steps

def calc_calorie(data):
	calories = 0.0
	for i in data['point']:
		calories+=(i['value'][0]['fpVal'])
	return int(calories)

def calc_distance(data):
	distance = 0.0
	for i in data['point']:
		distance+=(i['value'][0]['fpVal'])
	return int(distance)

def calc_height(data):
	height = 0
	for i in data['point']:
		height = i['value'][0]['fpVal']
	return int(height*100)

def calc_weight(data):
	weight = 0
	for i in data['point']:
		weight = i['value'][0]['fpVal']
	return int(weight)

def start(request):
	flag = False
	for i in OauthCreds.objects.all():
		if i.user == request.user:
			flag = True
	context = {}
	if not flag:
		context = { 'signed_in' : False , 'auth_url':'http://127.0.0.1:8000/fit/oauth'}
	else:
		context = oauthCallback(request)
	return render(request,'start.html',context)
def extra(request):
	return render(request,'extra.html')
def get_data_set():
	today = datetime.today().date()
	now = datetime.today()
	start = int(time.mktime(today.timetuple())*1000000000)
	end = int(time.mktime(now.timetuple())*1000000000)
	data_set = "%s-%s" % (start, end)
	return data_set

def oauthCallback(request):

	#print(q)
	scopes = ["https://www.googleapis.com/auth/contacts.readonly",
	"https://www.googleapis.com/auth/fitness.activity.read",
	"https://www.googleapis.com/auth/fitness.body.write",
	"https://www.googleapis.com/auth/fitness.location.write" ,
	"https://www.googleapis.com/auth/fitness.activity.write"
	]

	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    './credentials.json',
    scopes)
	flow.redirect_uri = 'http://127.0.0.1:8000/fit/oauth'
	isAuthorized = False
	for i in OauthCreds.objects.all():
		if i.user == request.user:
			isAuthorized = True
	if not isAuthorized:
		q = request.GET
		if not q:
			authorization_url, state = flow.authorization_url(
	    	access_type='offline',
	    	include_granted_scopes='true')
			return redirect(authorization_url)

		else:
			code = request.GET['code']
			flow.fetch_token(code = code)
			credentials = flow.credentials

			OauthCreds.objects.create(user = request.user,creds = credentials)

	else:
		print("herelmao",request.user.data.all()[0].user)
		print("here",request.user.data.all()[0].creds)
		credentials = request.user.data.all()[0].creds
	datasourceid_steps = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
	datasourceid_calories = "derived:com.google.calories.expended:com.google.android.gms:platform_calories_expended"
	datasourceid_distance = "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta"
	datasourceid_height = "raw:com.google.height:com.google.android.apps.fitness:user_input"
	datasourceid_weight = "raw:com.google.weight:com.google.android.apps.fitness:user_input"



	dataset = get_data_set()
	dataset1 = '0-'+dataset.split('-')[1]
	if credentials.expired:
		credentials.refresh(Request())

	#url  = "GET https://www.googleapis.com/fitness/v1/users/me/dataSources/%s/datasets/%s"%(datasourceid,dataset)
	fitness_service = build('fitness', 'v1', credentials = credentials)
	steps = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=datasourceid_steps, datasetId = dataset).execute()
	calories = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=datasourceid_calories, datasetId = dataset).execute()
	distance = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=datasourceid_distance, datasetId = dataset).execute()
	height = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=datasourceid_height, datasetId = dataset1).execute()
	weight = fitness_service.users().dataSources().datasets().get(userId='me', dataSourceId=datasourceid_weight, datasetId = dataset1).execute()

	steps = calc_step(steps)
	calories = calc_calorie(calories)
	distance = calc_distance(distance)
	height = calc_height(height)
	weight = calc_weight(weight)
		#steps+= int(i['value'][0]['intVal'])
	res = {"signed_in" : True, "step_count" : steps, "calories":calories , "distance" : distance, "height" : height, "weight" : weight}
		#steps+= int(i['value'][0]['intVal'])
	if isAuthorized:
		return res
	else:
		return redirect('auth_display')
		#response.json()
