from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Workouts
from exercise.models import Exercise

class WorkoutAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('user', None)
        super(WorkoutAddForm, self).__init__(*args, **kwargs)
        self.fields['exid'].queryset = Exercise.objects.filter(userid = self.username).order_by('title')
        self.fields['time'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'value' : date.today()})
         
    class Meta:
        fields = ['exid', 'c1', 'w1', 'c2', 'w2', 'time']
        model = Workouts