from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Fraternity(models.Model):
    name = models.CharField(max_length="200")

class Sport(models.Model):
    type = models.CharField(max_length="300",choices=(("basketball","Basketball"),("football","Flag Football")))

class Player(models.Model):
    user = models.ForeignKey(User)
    fraternity = models.ForeignKey(Fraternity)
    
class Team(models.Model):
    players = models.ManyToManyField(Player)
    
    def num_wins(self):
        return self.games_won.all().count()

class League(models.Model):
    teams = models.ManyToManyField(Team)
    sport = models.ForeignKey(Sport)
    season = models.CharField(max_length="300",choices=(("fall","Fall"),("spring","Spring")))

class Game(models.Model):
    teams = models.ManyToManyField(Team)
    winner = models.ForeignKey(Team,related_name="games_won")
    league = models.ForeignKey(League)

admin.site.register(Fraternity)
admin.site.register(Player)
admin.site.register(Sport)
admin.site.register(Team)
admin.site.register(League)
admin.site.register(Game)
