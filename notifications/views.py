# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from notifications.models import *
from notifications.forms import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    context={}
    context['notifForm'] = NotificationForm()
    return render(request,'index.html', context)

@csrf_exempt
def add_notif(request):
    f = NotificationForm(request.POST)
    context = {'notifForm': f}
    if not f.is_valid():
        return render(request, 'index.html', context)
    new_notif = f.save()
    return redirect('/notifs')

def get_notifs(request):
    notifs = Notification.objects.all().reverse()
    notifs = serializers.serialize('json', notifs)
    return HttpResponse(notifs, content_type="applicaion/json")

def accept_notif(request, uid):
    notif = Notification.objects.get(id=uid)
    notif.delete()
    return redirect('/notifs')
