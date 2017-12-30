from django.db import models
from django.contrib.auth.models import User

class Dinners(models.Model):
    dinner_author = models.ForeignKey(User, default = 1)
    dinners = models.CharField(max_length=264)
    recipe = models.TextField(blank=True)
    def __str__(self):
        return self.dinners


class DinnersDate(models.Model):


    dinner_user = models.ForeignKey(User, default = 1)
    din = models.ForeignKey('Dinners')
    date = models.DateField()
    def __str__(self):
        return str( self.din)+" "+str(self.date)

class UserSetting(models.Model):
    user = models.OneToOneField(User)
    setDays = models.CharField(max_length=8, default="13")
