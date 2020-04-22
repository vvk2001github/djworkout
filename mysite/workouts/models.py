from django.db import models
from exercise.models import Exercise

class Workouts(models.Model):
    exid = models.ForeignKey(Exercise, on_delete = models.CASCADE, related_name='workouts')
    c1 = models.IntegerField(default = 0)
    c2 = models.IntegerField(default = 0)
    w1 = models.FloatField(default = 0)
    w2 = models.FloatField(default = 0)
    time = models.DateTimeField(auto_now_add=True)
    
