from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from sports_tracking.models import Sport
from sports_tracking.models import Fraternity

def home(request):
    fraternities_list = Fraternity.objects.all()
    return render(request,"sports_tracking/home.html",{"fraternities_list": fraternities_list})

def sport_detail(request,slug):
    sport = get_object_or_404(Sport, slug=slug)
    return render(request,"sports_tracking/sport_detail.html",{"sport":sport})
