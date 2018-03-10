from django.conf.urls import url, include
from django.contrib import admin
from notifications.views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^add_notif$', add_notif),
    url(r'^get_notifs$', get_notifs),
    url(r'^accept_notif/(?P<uid>\d+)$', accept_notif),
]