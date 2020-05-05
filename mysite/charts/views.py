""" Module docstring """
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Sum
from django.shortcuts import render, get_object_or_404
from exercise.models import Exercise
from workouts.models import Workouts

@login_required(login_url='/login')
def chart01(request):
    """ Index """
    exercises_w = Exercise.objects.filter(userid=request.user).filter(types='W')
    return render(request, 'charts/chart01.html', {'dataset1' : exercises_w})

@login_required(login_url='/login')
def chartmax(request, pk_value):
    """ Maximum count in exercise """
    exercise = get_object_or_404(Exercise, pk=pk_value)
    workouts = Workouts.objects.filter(exid=exercise.pk).order_by('time'). \
        values('time').annotate(max_count=Max('c1'))
    labels_list = [date.strftime("%Y-%m-%d") for date in workouts.values_list('time', flat=True)]
    data_list = list(workouts.values_list('max_count', flat=True))
    return render(request, 'charts/chartmax.html',
                  {'exercise': exercise, 'labels_list' : labels_list, 'data_list' : data_list})

@login_required(login_url='/login')
def chartsum(request, pk_value):
    """ Sum count in exercise """
    exercise = get_object_or_404(Exercise, pk=pk_value)
    workouts = (
        Workouts.objects.filter(exid=exercise.pk)
        .order_by('time').values('time')
        .annotate(max_count=Sum('c1'))
    )
    labels_list = [date.strftime("%Y-%m-%d") for date in workouts.values_list('time', flat=True)]
    data_list = list(workouts.values_list('max_count', flat=True))
    return render(request, 'charts/chartsum.html',
                  {'exercise': exercise, 'labels_list' : labels_list, 'data_list' : data_list})

@login_required(login_url='/login')
def chartdetail(request, pk_value):
    """ Count in exercise """
    exercise = get_object_or_404(Exercise, pk=pk_value)
    workouts = Workouts.objects.filter(exid=exercise.pk).order_by('time')
    labels_list = [date.strftime("%Y-%m-%d") for date in workouts.values_list('time', flat=True)]
    data_list = list(workouts.values_list('c1', flat=True))
    return render(request, 'charts/chartdetail.html',
                  {'exercise': exercise, 'labels_list' : labels_list, 'data_list' : data_list})
