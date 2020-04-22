from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    EXTYPES = [
        ('W', 'Without Weight'),
        ('WW', 'With Weight'),
        ('LR', 'LeftRight Without Weight'),
        ('LRW', 'LeftRight Weight')
    ]

    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')
    title = models.CharField(max_length = 120, help_text = 'Title of exercise.')
    types = models.CharField(max_length = 3, choices = EXTYPES)

    def __str__(self):
        return self.title