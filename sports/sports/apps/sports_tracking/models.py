

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
    TENNIS = 'TS'
    ULTIMATE_FRISBEE = 'UF'
    WRESTLING= 'WG'
    TRACK = 'TK'
    SPORTS_TRIVIA = 'ST'
    SWIMMING = 'SG'
    BOWLING = 'BG'
    SPORTS_CHOICES = (
        (BASKETBALL, 'Basketball'),
        (FLAG_FOOTBALL, 'Flag Football'),
        (VOLLEYBALL, 'Volleyball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
        (HOCKEY, 'Hockey'),
        (TENNIS, 'Tennis'),
        (ULTIMATE_FRISBEE, 'Ultimate Frisbee'),
        (WRESTLING, 'Wrestling'),
        (TRACK, 'Track'),
        (SPORTS_TRIVIA, 'Sports Trivia'),
        (SWIMMING, 'Swimming'),
        (BOWLING, 'Bowling'),
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

    is_major = models.BooleanField(default=True)


    def display(self):
        return self.get_type_display()

    def __unicode__(self):
        return self.display()

class Player(models.Model):
    user = models.ForeignKey(User)
    def __unicode__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username
    
class Team(models.Model):
    players = models.ManyToManyField(Player)
    name = models.CharField(null=True,blank=True,max_length=200)
    
    def num_wins(self):
        return self.games_won.all().count()
    def __unicode__(self):

        if self.name:

            return self.name
        elif len(self.fraternity_set.all())>0:
            return self.fraternity_set.all()[0].name
        else:
            return ", ".join([p.__unicode__() for p in self.players.all()])

class Game(models.Model):
    visitor_team = models.ForeignKey(Team, related_name="visitor_team")
    home_team = models.ForeignKey(Team, related_name="home_team")
    winner = models.ForeignKey(Team,related_name="games_won",null=True,blank=True)
    is_tie = models.BooleanField(default=False)
    sport = models.ForeignKey(Sport)
    parent = models.ForeignKey("self",null=True,blank=True)
    location = models.CharField(max_length="200")
    date = models.DateTimeField()

class Fraternity(models.Model):
    name = models.CharField(max_length="200")
    teams = models.ManyToManyField(Team)

    def overall_points_for_sport(self,sport):

        points = 0

        for team in self.teams.all():
            points += team.games_won.filter(sport=sport).count()
        return points
    def stats_for_sport(self,sport):
        """
            Compiles some data about this fraternity for a given sport.

            Not sure what to do about "points" yet. How is this calculated?
        """
        data = {"wins":0,"losses":0,"ties":0,"points":0}
        for team in self.teams.all():
            for game in list(team.visitor_team.all())+list(team.home_team.all()):
                if game.winner is team:
                    data['wins']+=1

                elif game.is_tie:
                    data['ties']+=1

                else:
                    data['losses']+=1
        return data
    def overall_points(self,major_only=True):
        points = 0
        for team in self.teams.all():
            if major_only:
                points += team.games_won.filter(sport__is_major=True).count()
            else:
                points += team.games_won.all().count()
        return points
    def rank(self):
        frats = Fraternity.objects.all()
        sorted_frats = sorted(frats, key=lambda f: f.overall_points())
        return 1+sorted_frats.index(self)
    def __unicode__(self):
        return self.name

class Meeting(models.Model):
    description = models.TextField(null=True)
    date = models.DateTimeField()
    fraternities_attended = models.ManyToManyField(Fraternity)

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

class Contact(models.Model):

    fraternity = models.ForeignKey(Fraternity)
    contact_name = models.CharField(max_length="200")
    contact_number = models.CharField(max_length="200")

    def __unicode__(self):
        return self.fraternity.name

admin.site.register(Fraternity)
admin.site.register(Group)
admin.site.register(Player)
admin.site.register(Sport)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Meeting)
admin.site.register(Contact)
