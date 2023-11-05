from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DURATION_CHOICES  = (
  ('15 Minutes', '15 Minutes'),
  ('30 Minutes', '30 Minutes'),
  ('45 Minutes', '45 Minutes'),
  ('1 Hour', '1 Hour'),
  ('1.5 Hours', '1.5 Hours'),
  ('2 Hours', '2 Hours'),
  ('More than 2 Hours', 'More than 2 Hours'),
)

WORKOUT_TYPE_CHOICES = [
    ('cardio', 'Cardio'),
    ('weightlifting', 'Weightlifting'),
    ('flexibility', 'Flexibility'),
    ('HIIT', 'High-Intensity Interval Training'),
    ('yoga', 'Yoga'),
    ('pilates', 'Pilates'),
    ('swimming', 'Swimming'),
    ('cycling', 'Cycling'),
    ('walking', 'Walking'),
    ('other', 'Other'),
]


# Create your models here.

class Workout(models.Model):
  date = models.DateField()
  # title = models.CharField(max_length=100)
  duration = models.CharField(
    max_length=50,
    choices=DURATION_CHOICES,
    default=DURATION_CHOICES[0][0]
  )
  description = models.CharField(max_length=1000)
  workout_type = models.CharField(
        max_length=20,
        choices=WORKOUT_TYPE_CHOICES,
        default=WORKOUT_TYPE_CHOICES[0][0]
    )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('workout-detail', kwargs={'workout_id': self.id})
  
  def worked_out_today(self):
    today = date.today()
    return Workout.objects.filter(user=self.user, date=today).exists()
  

class Set(models.Model):
  rep = models.IntegerField()
  movement = models.CharField(max_length=250)
  weight = models.IntegerField()
  equipment = models.CharField(max_length=100)
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.movement} with {self.rep} reps"


