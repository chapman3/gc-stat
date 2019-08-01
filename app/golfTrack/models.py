from django.db import models

# Create your models here.

class Hole(models.Model):
    par = models.IntegerField()
    distance = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    # Add Holes

class Scores(models.Model):
    vs_par = models.IntegerField()
    # Add Shots by hole

class Round(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    scores = models.ForeignKey(Scores, on_delete=models.CASCADE)

class Scorecard(models.Model):
    date = models.DateField()
    the_round = models.ForeignKey(Round, on_delete=models.CASCADE)