""" Docstring """
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from exercise.models import Exercise
from .models import Workouts
from .forms import WorkoutAddForm

class IndexView(LoginRequiredMixin, ListView):
    """ Docstring pylint """
    login_url = '/login/'
    template_name = 'workouts/index.html'
    context_object_name = 'workouts_list'
    paginate_by = 10
    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Workouts.objects.raw('SELECT w.*, e.title, e.types FROM workouts_workouts w, \
                                    exercise_exercise e, auth_user a where (w.exid_id = e.id) \
                                        and(a.id = e.userid_id)and(a.username = %s) \
                                            order by w.time DESC', [user.username])

#Workout Detail View
class WorkoutDetailView(LoginRequiredMixin, DetailView):
    """ Docstring pylint """
    login_url = '/login/'
    model = Workouts
    template_name = 'workouts/work-detail.html'

@login_required(login_url='/login')
def workoutadd(request):
    """ Docstring pylint """
    if request.method == 'POST':
        form = WorkoutAddForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('workouts:index')
        else:
            print('FORM NOT VALID')
    datadict = dict()
    if request.user is not None:
        form = WorkoutAddForm(user=request.user)
        user = get_object_or_404(User, username=request.user)
        tmp = Exercise.objects.filter(userid=user).values('id', 'types')
        for i in tmp:
            datadict[i['id']] = i['types']

    return render(request, 'workouts/work-add.html', {'form' : form, 'datadict' : datadict})

@login_required(login_url='/login')
def edit(request, pk_value):
    """ Docstring pylint """
    workout = get_object_or_404(Workouts, pk=pk_value)
    form = WorkoutAddForm(request.POST or None, instance=workout, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('workouts:index')

    datadict = dict()
    if request.user is not None:
        user = get_object_or_404(User, username=request.user)
        tmp = Exercise.objects.filter(userid=user).values('id', 'types')
        for i in tmp:
            datadict[i['id']] = i['types']
    return render(request, 'workouts/work-edit.html', {'form' : form, 'datadict' : datadict})

@login_required(login_url='/login')
def delete(request, pk_value):
    """ Docstring pylint """
    workout = get_object_or_404(Workouts, pk=pk_value)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts:index')
    return render(request, 'workouts/work-delete.html', {'object' : workout})
