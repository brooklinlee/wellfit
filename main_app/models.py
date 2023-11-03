from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# DURATION  = (
#   ('A', '15 Minutes'),
#   ('B', '30 Minutes'),
#   ('C', '45 Minutes'),
#   ('D', '1 Hour'),
#   ('E', '1.5 Hours'),
#   ('F', '2 Hours'),
#   ('G', 'More than 2 Hours'),
# )

# Create your models here.

class Workout(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=100)
  # duration = models.CharField(
  #   max_length=50,
  #   choices=DURATION,
  #   default=DURATION[0][0]
  # )
  duration = models.DurationField(default="0:00")
  description = models.CharField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('workout-detail', kwargs={'workout_id': self.id})
  
  def worked_out_today(self):
    return self.workout_set.filter(date=date.today()).count() >= 1
  

class Set(models.Model):
  rep = models.IntegerField()
  movement = models.CharField(max_length=250)
  equipment = models.CharField(max_length=100)
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.movement} with {self.rep} reps"
  

