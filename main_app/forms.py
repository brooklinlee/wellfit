from django.forms import ModelForm
from .models import Set, Workout
from django import forms

class SetForm(ModelForm):
  class Meta:
    model = Set
    fields = ['rep', 'movement', 'weight', 'equipment'] 

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'title', 'duration', 'description']

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))