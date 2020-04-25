from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Workouts
from exercise.models import Exercise

class WorkoutAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('user', None)
        super(WorkoutAddForm, self).__init__(*args, **kwargs)
        self.user = get_object_or_404(User, username = self.username)
        self.fields['exid'].queryset = Exercise.objects.filter(userid = self.user).order_by('title')
         

    class Meta:
        fields = ['exid', 'c1', 'w1', 'c2', 'w2']
        model = Workouts