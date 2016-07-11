import pyowm
import requests
from datetime import date
from dateutil.rrule import rrule, DAILY
API_KEY="68897584b12c57a6f018081baac462c2"
################### GET CUURENT WEATHER DETAILS     ############################
x=raw_input("Enter any place to get current weather :")
owm = pyowm.OWM(API_KEY)
observation = owm.weather_at_place(x)
w = observation.get_weather()
humidity=w.get_humidity()
temperature=w.get_temperature('celsius')
print str(temperature['temp'])+ " degree celsius"
print humidity
################################################################################

######################## GET DATA ACCORDING TO DATE ############################
location=raw_input("Enter any place to get weather according date :")
def get_json():
    ########## WE CAN CHANGE DATE HERE #########################################
    a = date(2015, 1, 1)
    b = date(2015, 12, 31)
    for dt in rrule(DAILY, dtstart=a, until=b):
        get_weather(dt.strftime("%Y%m%d"))
def get_weather(find_date):
    urlstart = 'http://api.wunderground.com/api/9f531938a5579c5e/history_'
    urlend = '/q/Switzerland/Zurich.json'
    url = urlstart + str(find_date) + urlend
    data = requests.get(url).json()
    for summary in data['history']['dailysummary']:
        print ','.join((gooddate,summary['date']['year'],summary['date']['mon'],summary['date']['mday'],summary['precipm'], summary['maxtempm'], summary['meantempm'],summary['mintempm']))
################################################################################
