# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notification(models.Model):
    """docstring for Notification"""
    name = models.CharField(max_length=100, null=False)
    room_num = models.CharField(max_length=10, null=False)
    category = models.CharField(max_length=100, null=False, 
                                    choices=[('pw','Paperwork'),
                                             ('pr','Printing'),
                                             ('rf','Refreshments')])
    comments = models.TextField()


