from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExerciseForm
from .models import Exercise
from django.contrib.auth.models import User

class IndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name='exercise/index.html'
    context_object_name = 'exercise_list'
    def get_queryset(self):
        self.userid = get_object_or_404(User, username = self.request.user)
        return Exercise.objects.filter(userid = self.userid).order_by('title')

#Create new Exercise
@login_required(login_url='/login')
def postview(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():           
            form.save()
            return redirect('exercise:index')
    form = ExerciseForm()
    form.initial['userid'] = get_object_or_404(User, username = request.user)
    return render(request, 'exercise/post.html', {'form' : form})

#Exercise Detail View
class ExerciseDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model=Exercise
    template_name = 'exercise/exercise-detail.html'

#Edit Exercise
@login_required(login_url='/login')
def edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    form = ExerciseForm(request.POST or None, instance = exercise)
    if form.is_valid():
        form.save()
        return redirect('exercise:index')
    return render(request, 'exercise/edit.html', {'form' : form})

#Delete Exercise
@login_required(login_url='/login')
def delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)    
    if request.method=='POST':
        exercise.delete()
        return redirect('exercise:index')
    return render(request, 'exercise/exercise-delete.html', {'object' : exercise})