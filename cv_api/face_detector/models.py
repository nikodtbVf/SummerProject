from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	work = models.TextField()
	cellphone = models.CharField(max_length=12)
	street = models.CharField(max_length=50)
	number_house = models.IntegerField()
	colony = models.CharField(max_length=50)
	postalcode = models.IntegerField()
	municipality = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False,auto_now= True)

	def __str__(self):
		return self.name

class Image(models.Model):
	urlimage = models.TextField()
	hand = models.CharField(max_length=20)
	finger = models.IntegerField()
	person = models.ForeignKey(Person)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False,auto_now= True)

	def __str__(self):
		return self.urlimage

class User(models.Model):
	name = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	def __str__(self):
		return self.name
