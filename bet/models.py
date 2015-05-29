from django.db import models
from user.models import *
import datetime
# Create your models here.

class UserBet(models.Model):
	description=models.CharField(max_length=2000)
	on=models.DateTimeField(auto_now_add=True)
	by=models.ForeignKey(UserProfile,related_name="added_by")
	moderator=models.ForeignKey(UserProfile,related_name="mod",blank=True)
	likers=models.ManyToManyField(UserProfile,related_name="liked_by",blank=True)
	participantCount=models.IntegerField(default=0)
	resultTime=models.DateTimeField(blank=True)
	result=Models.CharField(max_length=500)
	addMoreOptions=models.BooleanField(default=False)
	
class Options(models.Model):
	optionText=models.CharField(max_length=500)
	optionToBet=models.ForeignKey(UserBet)
	participants=models.ManyToManyField(UserProfile,blank=True)
	optionCount=models.IntegerField(default=0)

class Comment(models.Model):
	commentText=models.CharField(max_length=500)
	commentAddedOn=models.DateTimeField(auto_now_add=True)
	commentBy=models.ForeignKey(UserProfile,related_name="comment_by")
	commentLikers=models.ManyToManyField(UserProfile,related_name="liked_by",blank=True)
	commentToBet=models.foreignKey(UserBet)
	
	


