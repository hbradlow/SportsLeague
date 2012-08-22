from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from sports_tracking.views import *

urlpatterns = patterns('sports_tracking.views',
    url(r'^$', home,name="home"),
    url(r'^flag_football$', flag_football, name="flag_football"),
    url(r'^volleyball/$', volleyball, name="volleyball"),
    url(r'^basketball/$', basketball, name="basketball"),
    url(r'^soccer/$', soccer, name="soccer"),
    url(r'^softball/$', softball, name="softball"),
    url(r'^hockey/$', hockey, name="hockey"),
)
