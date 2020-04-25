from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Workouts
from .forms import WorkoutAddForm
from django.contrib.auth.models import User
from exercise.models import Exercise

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

@login_required(login_url='/login')
def workoutadd(request):
    if request.method == 'POST':
        form = WorkoutAddForm(request.POST)
        if form.is_valid():           
            form.save()
            return redirect('workouts:index')
    form = WorkoutAddForm(user=request.user)
    user = get_object_or_404(User, username = request.user)
    tmp = Exercise.objects.filter(userid = user).values('id', 'types')
    datadict = dict()
    for i in tmp:
        datadict[i['id']] = i['types']
    #print(datadict)
    return render(request, 'workouts/work-add.html', {'form' : form, 'datadict' : datadict})
