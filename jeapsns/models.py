#coding=utf-8
from django.db import models

class Pub(models.Model):
	name           = models.CharField(max_length=30)
	address        = models.CharField(max_length=50)
	city           = models.CharField(max_length=60)


class content(models.Model):
	username     = models.CharField(max_length=30)
	image        = models.CharField(max_length=256)
	updated      = models.DateTimeField(auto_now_add=True)
	created      = models.DateTimeField(auto_now=True)
	text         = models.TextField()


class meg(models.Model):
    username    = models.CharField(max_length =30)
    contentid   = models.IntegerField()
    status      = models.IntegerField()
