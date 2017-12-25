from django.db import models
from django.contrib.auth.models import User

class Dinners(models.Model):
    dinners = models.CharField(max_length=264)
    def __str__(self):
        return self.dinners
class DinnersDate(models.Model):
    din = models.ForeignKey(Dinners)
    date = models.DateField()
    def __str__(self):
        return str( self.din)+" "+str(self.date)
