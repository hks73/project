from django.shortcuts import render,render_to_response
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
try:
    from django.utils import simplejson as json
except:
    import simplejson as json
import sys
from weather.models import weatherDetails
# Create your views here.
from datetime import date
from dateutil.rrule import rrule, DAILY
import requests
import pyowm
import openweather
from datetime import datetime
import json,ast,codecs
from django.db import connection
from weather.models import *
API_KEY="68897584b12c57a6f018081baac462c2"

humidity=0
temperature=0
def search(request):
    if 'q' in request.GET and request.GET['q']:
        x=request.GET['q']
        owm = pyowm.OWM(API_KEY)
        observation = owm.weather_at_place(x)
        w = observation.get_weather()
        humidity=w.get_humidity()
        temperature=w.get_temperature('celsius')
        p=weatherDetails()
        p.humid=humidity
        p.temp=temperature
        p.location=x
        p.save()
        ow = openweather.OpenWeather()
        start_date = datetime(2013, 9, 10)
        end_date = datetime(2013, 9, 15)

        cursor = connection.cursor()
        cursor.execute('select station_id from weather_stations where station_name = %s',[x])
        result=cursor.fetchall()
        print "harsh"
        station_id= int(result[0][0])
        print station_id
        print type(station_id)
        a= ow.get_historic_weather(station_id, start_date, end_date,"day")
        my_list=[]
        for i,value in enumerate(a):
            my_list.append(value["temp"]["ma"])
        print my_list
        return render_to_response('weather_website.html',
    								{'current_humidity':humidity,'current_temperature':temperature['temp'],'get_list':my_list}	)
    else:
        message = 'You submited an empty form'
        print("AAAAAAH")
        return render(request, 'weather_website.html', {'msg':message})
# def get_weather(request):
#      if 'q' in request.GET and request.GET['q']:
#          x=request.GET['q']
#
#          # default: hourly interval

#          result=cursor.fetchall()
#
#     if 'q' in request.GET and request.GET['q']:
#         x=request.GET['q']
#         urlstart = 'http://api.wunderground.com/api/9f531938a5579c5e/history_'
#         urlend = '/q/Switzerland/Zurich.json'
#         url = urlstart + str(gooddate) + urlend
#         data = requests.get(url).json()
#         for summary in data['history']['dailysummary']:
#             print ','.join((gooddate,summary['date']['year'],summary['date']['mon'],summary['date']['mday']]))
#         return render_to_response('user.html',
#     								{'current_humidity':humidity,'current_temperature':temperature['temp']}	)
#     else:
#         message = 'YOU submited an empty form of DATE'
#         return render(request, 'user.html', {'msg2':message})
# def get_json(request):
#     a = date(2013, 1, 1)
#     b = date(2013, 12, 31)
#     for dt in rrule(DAILY, dtstart=a, until=b):
#         get_weather(dt.strftime("%Y%m%d"))
