from django.db import models

class ClubMember(models.Model):
    
    username = models.IntegerField()
    clubname = models.CharField(max_length = 100)
    balance = models.FloatField(max_length= 100)
    password = models.CharField(max_length = 100)
    
    def __int__(self):
        return self.username

class Movie(models.Model):
    
    movie = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    rating= models.CharField(max_length = 3)
    dateShowing = models.DateTimeField()
    seats = models.IntegerField()
    
    def __int__(self):
        return self.movie + '' + self.description + self.rating