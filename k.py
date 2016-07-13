import urllib
import urllib2
import csv
from bs4 import BeautifulSoup
a= urllib2.urlopen("http://openweathermap.org/city/1712808")
soup = BeautifulSoup(a,"lxml")
