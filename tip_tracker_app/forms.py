from django import forms

from .models import *

class Tip_Form(forms.ModelForm):
    class Meta:
        model = Tip_Entry
        fields = ['tip', 'type']
        labels = {'text': ''}