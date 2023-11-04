from django.forms import ModelForm, NumberInput
from .models import Set, Workout
from django import forms

class SetForm(ModelForm):
  class Meta:
    model = Set
    fields = ['rep', 'movement', 'weight', 'equipment'] 
    widgets = {
      'rep': NumberInput(attrs={'step': 1}),
      'weight': NumberInput(attrs={'step': 5}),
    }


class WorkoutForm(forms.ModelForm):
  class Meta:
    model = Workout
    fields = ['date', 'title', 'workout_type', 'duration', 'description']

  date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
