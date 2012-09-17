from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from sports_tracking.views import *

urlpatterns = patterns('sports_tracking.views',
    url(r'^$', home,name="home"),
    url(r'^sport/(?P<slug>[\w\._-]+)/$', sport_detail, name="sport_detail"),
)
