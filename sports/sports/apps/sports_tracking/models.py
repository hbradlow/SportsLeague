from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.fields import *
from django.contrib import admin


class Sport(models.Model):
    BASKETBALL = 'BB'
    FLAG_FOOTBALL = 'FF'
    VOLLEYBALL = 'VB'
    SOCCER = 'SR'
    SOFTBALL = 'SB'
    HOCKEY = 'HY'
    SPORTS_CHOICES = (
        (BASKETBALL, 'Basketball'),
        (FLAG_FOOTBALL, 'Flag Football'),
        (VOLLEYBALL, 'Volleyball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
        (HOCKEY, 'Hockey'),
    )
    type = models.CharField(max_length="300",choices=SPORTS_CHOICES, default=BASKETBALL)
    slug = AutoSlugField(populate_from="type",unique=True)

    FALL = 'FL'
    WINTER = 'WR'
    SPRING = 'SG'
    SEASON_CHOICES = (
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
    )
    season = models.CharField(max_length="300", choices=SEASON_CHOICES, default=FALL)

    def display(self):
        return self.get_type_display()

    def __unicode__(self):
        return self.display()

class Player(models.Model):
    user = models.ForeignKey(User)
    
class Team(models.Model):
    players = models.ManyToManyField(Player)
    
    def num_wins(self):
        return self.games_won.all().count()

class Game(models.Model):
    teams = models.ManyToManyField(Team)
    winner = models.ForeignKey(Team,related_name="games_won")
    sport = models.ForeignKey(Sport)

class Fraternity(models.Model):
    name = models.CharField(max_length="200")
    teams = models.ManyToManyField(Team)

    def overall_points_for_sport(self,sport):
        points = 0
        for team in self.teams.all():
            points += team.games_won.filter(sport=sport).count()
        return points
    def __unicode__(self):
        return self.name

class Group(models.Model):
    GROUP_A = 'A'
    GROUP_B = 'B'
    GROUP_CHOICES = (
        (GROUP_A, 'Group A'),
        (GROUP_B, 'Group B'),
    )
    group = models.CharField(max_length="300", choices=GROUP_CHOICES, default=GROUP_A)
    fraternities = models.ManyToManyField(Fraternity)
    sport = models.ForeignKey(Sport)
    def display(self):
        return self.get_group_display()

    def __unicode__(self):
        return self.display()

admin.site.register(Fraternity)
admin.site.register(Group)
admin.site.register(Player)
admin.site.register(Sport)
admin.site.register(Team)
admin.site.register(Game)

