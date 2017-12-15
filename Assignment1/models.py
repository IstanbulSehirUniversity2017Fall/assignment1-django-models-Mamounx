# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Games(models.Model):
    director = models.CharField(max_length=25)
    game_name = models.CharField(max_length=25)
    genre = models.CharField(max_length=10)
    game_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_name + " - " + self.director

class horrorGame(models.Model):
    frenchise = models.ForeignKey(Games, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=25)