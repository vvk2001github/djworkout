from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from exercise.models import Exercise
from workouts.models import Workouts

@login_required(login_url='/login')
def chart01(request):    
    exercises = Exercise.objects.filter(userid = request.user).filter(types='W')
    return render(request, 'charts/chart01.html', {'dataset1' : exercises})

@login_required(login_url='/login')
def chart02(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    workouts = Workouts.objects.filter(exid = exercise.pk)
    labels_list = [date.strftime("%Y-%m-%d") for date in workouts.values_list('time', flat=True)]
    data_list = list(workouts.values_list('c1', flat = True))
    return render(request, 'charts/chart02.html', {'exercise': exercise, 'labels_list' : labels_list, 'data_list' : data_list})
