from django.forms import ModelForm
from notifications.models import Notification

class NotificationForm(ModelForm):
    """docstring for NotificationForm"""
    class Meta:
        model = Notification
        fields = ['name', 'room_num', 'category', 'comments']

        