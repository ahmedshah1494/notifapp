# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from notifications.models import *
from notifications.forms import *

# Create your views here.
def home(request):
    # if request.method != 'GET':
    #     return HttpResponse("", status=400)
    context={}
    context['notifForm'] = NotificationForm()
    return render(request,'index.html', context)

def add_notif(request):
    # if request.method != 'POST':
    #     return HttpResponse("", status=400)

    f = NotificationForm(request.POST)
    context = {'notifForm': f}
    if not f.is_valid():
        return render(request, 'index.html', context)
    new_notif = f.save()
    return redirect('/notifs')

def get_notifs(request):
    # if request.method != 'GET':
    #     return HttpResponse("", status=400)
    notifs = Notification.objects.all().reverse()
    notifs = serializers.serialize('json', notifs)
    return HttpResponse(notifs, content_type="applicaion/json")

def accept_notif(request, uid):
    # if request.method != 'GET':
    #     return HttpResponse("", status=400)
    notif = Notification.objects.get(id=uid)
    notif.delete()
    return redirect('/notifs')
