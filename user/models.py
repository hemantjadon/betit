from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


#### User Model ####
class BetitUser(AbstractUser):
    gender = models.CharField(max_length=1,blank=True)
    dob = models.DateField(default = datetime.datetime.now())
    def get_full_name(self):
        return self.first_name+' '+self.last_name


class UserProfile(models.Model):
    user=models.OneToOneField(BetitUser)
    phone_no=models.CharField(max_length=15,null=False)  #Take Phone Number Field
    image=models.ImageField(upload_to = 'profile_pics/',blank = True) # FK to user model
    
#### Hash Tags Model ####
class hashTags(models.Model):
        name = models.CharField(max_length=100 ,null=False)
        count = models.IntegerField(default = 0)
        def __str__(self):
            return '#'+self.name


#### Photos Model ####


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'uploads/')
    by=models.ForeignKey(UserProfile,related_name='uploaded_by')
    on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=10000,null = True)
    user_tags= models.ManyToManyField(UserProfile,related_name='tagged_in')
    likers=models.ManyToManyField(UserProfile,related_name='liker')
    
    def __str__(self):
        return "By: "+self.by.username


class Workplace(models.Model):
    name=models.CharField(max_length=100,null=False)
    count = models.IntegerField(default=0)
    user = models.ManyToManyField(UserProfile,related_name='work')
    
