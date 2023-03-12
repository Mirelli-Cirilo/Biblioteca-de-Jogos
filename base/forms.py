from django import forms

from .models import *

class Gameform(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

