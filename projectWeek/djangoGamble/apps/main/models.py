import json
from django.db import models
from django.utils import timezone

class Game(models.Model):
    images = models.CharField(max_length=255)
    team_names = models.CharField(max_length=255)
    dates = models.CharField(max_length=60)

