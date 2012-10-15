from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from sports_tracking.models import Sport
from sports_tracking.models import Fraternity
from sports_tracking.models import Contact

def home(request):
    fraternities_list = Fraternity.objects.all()
    return render(request,"sports_tracking/home.html",{"fraternities_list": fraternities_list})

def sport_detail(request,slug):
    sport = get_object_or_404(Sport, slug=slug)
    return render(request,"sports_tracking/sport_detail.html",{"sport":sport})

def flag_football(request):
    fraternities_list = Fraternity.objects.all()
    return render(request,"sports_tracking/flag_football.html",{"fraternities_list": fraternities_list})

def volleyball(request):
    return render(request,"sports_tracking/volleyball.html")

def basketball(request):
    return render(request,"sports_tracking/basketball.html")

def soccer(request):
    return render(request,"sports_tracking/soccer.html")

def softball(request):
    return render(request,"sports_tracking/softball.html")

def hockey(request):
    return render(request,"sports_tracking/hockey.html")

def handbook(request):
    return render(request,"sports_tracking/handbook.html")

def contacts(request):
    contacts_list= Contact.objects.all()
    return render(request,"sports_tracking/contacts.html",{"contacts_list": contacts_list})
