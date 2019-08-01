from django.db import models

# Create your models here.

class Hole(models.Model):
    par = models.IntegerField()
    distance = models.IntegerField()
    def __str__(self):
        return "Hole Model"

class Course(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    # Add Holes
    def __str__(self):
        return self.name

class Scores(models.Model):
    vs_par = models.IntegerField()
    # Add Shots by hole
    def __str__(self):
        return "Scores Model"

class Round(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    scores = models.ForeignKey(Scores, on_delete=models.CASCADE)
    def __str__(self):
        return "Round Model for " + self.course.name

class Scorecard(models.Model):
    date = models.DateField()
    the_round = models.ForeignKey(Round, on_delete=models.CASCADE)
    def __str__(self):
        return "Scorecard for " + self.the_round.__str__() + " on " + self.date.isoformat()