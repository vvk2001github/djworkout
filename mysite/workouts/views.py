from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Workouts
from exercise.models import Exercise
from django.contrib.auth.models import User

class IndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name='workouts/index.html'
    context_object_name = 'workouts_list'
    def get_queryset(self):
        self.user = get_object_or_404(User, username = self.request.user)
        return Workouts.objects.raw('SELECT w.*, e.title, e.types FROM workouts_workouts w, exercise_exercise e, auth_user a where (w.exid_id = e.id)and(a.id = e.userid_id)and(a.username = %s)', [self.user.username])

#Workout Detail View
class WorkoutDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model=Workouts
    template_name = 'workouts/work-detail.html'
