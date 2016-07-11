from __future__ import unicode_literals

from django.db import models

class weatherDetails(models.Model):
    	location  =  models.TextField()
    	temp      =  models.TextField()
        humid     =  models.TextField()

# Create your models here.
