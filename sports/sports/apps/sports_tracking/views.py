from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from sports_tracking.models import Sport
from sports_tracking.models import Fraternity
def home(request):
    sport_FF = Sport.objects.get(type="FF").display()
    sport_VB = Sport.objects.get(type="VB").display()
    sport_BB = Sport.objects.get(type="BB").display()
    sport_SR = Sport.objects.get(type="SR").display()
    sport_SB = Sport.objects.get(type="SB").display()
    sport_HY = Sport.objects.get(type="HY").display()
    fraternities_list = Fraternity.objects.all()
    return render_to_response("sports_tracking/home.html",{"sport_FF": sport_FF, "sport_VB": sport_VB, "sport_BB": sport_BB, "sport_SR": sport_SR, "sport_SB": sport_SB, "sport_HY": sport_HY, "fraternities_list": fraternities_list},)

def flag_football(request):
    return render_to_response("sports_tracking/flag_football.html")

def volleyball(request):
    return render_to_response("sports_tracking/volleyball.html")

def basketball(request):
    return render_to_response("sports_tracking/basketball.html")

def soccer(request):
    return render_to_response("sports_tracking/soccer.html")

def softball(request):
    return render_to_response("sports_tracking/softball.html")

def hockey(request):
    return render_to_response("sports_tracking/hockey.html")
