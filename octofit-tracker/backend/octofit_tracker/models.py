from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'octofit_tracker_team'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        db_table = 'octofit_tracker_activity'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'octofit_tracker_leaderboard'
        verbose_name = 'Leaderboard'
        verbose_name_plural = 'Leaderboards'
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'octofit_tracker_workout'
        verbose_name = 'Workout'
        verbose_name_plural = 'Workouts'
    def __str__(self):
        return self.name
