from django.db import models
from exercise.models import Exercise

class Workouts(models.Model):
    exid = models.ForeignKey(Exercise, on_delete = models.CASCADE, related_name='workouts', verbose_name = 'Упражнения')
    c1 = models.IntegerField(default = 0, verbose_name = 'Повторов левых')
    c2 = models.IntegerField(default = 0, verbose_name = 'Повторов правых')
    w1 = models.FloatField(default = 0, verbose_name = 'Вес левый')
    w2 = models.FloatField(default = 0, verbose_name = 'Вес правый')
    time = models.DateField(auto_now_add=False)
    
    