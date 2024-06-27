from django.db import models
from django.contrib.auth import get_user_model
from datetime import time
from django.shortcuts import render
from django.utils import timezone


# Create your models here.

class Message(models.Model):
	recipient = models.ManyToManyField(get_user_model())
	sender = models.ManyToManyField(get_user_model())
	timestamp = models.DateTimeField(auto_now_add=True)
	subject = models.CharField(max_length=255)
	body = models.CharField(max_length=300)
	   
	def __str__(self):
		return self.subject  
	  
	#   Time Stamp: From sender to Receipient subject
	  
class File(models.Model):
	message = models.ForeignKey(Message, related_name='files', on_delete=models.CASCADE)
	file = models.FileField(upload_to='PATH_NAME')
	  
	def __str__(self):
		return self.file.name