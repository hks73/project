from __future__ import unicode_literals

from django.db import models

class weatherDetails(models.Model):
    	location  =  models.TextField()
    	temp      =  models.TextField()
        humid     =  models.TextField()
class Stations(models.Model):
    station_id    =   models.IntegerField()
    station_name  =   models.CharField(max_length=250)
# Create your models here.
