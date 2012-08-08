from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse

def home(request):
    return render_to_response("sports_tracking/home.html",context_instance=RequestContext(request))
