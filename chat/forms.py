from django import forms
from . import models

class Insert(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ['username1','username2','attach']