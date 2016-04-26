from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255,null=True,blank=True,unique=True)
	date = models.DateTimeField(auto_now_add=True)
	tags = models.TextField(max_length=1000,null=True,blank=True)
	article = models.TextField(max_length=1000,null=True,blank=True)
	author = models.ForeignKey(User,null=True,blank=True)
