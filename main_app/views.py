from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Set
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse
from .forms import SetForm, WorkoutForm


# PROTECT ROUTES: 
# def (view functions): @login_required
# class(class-based views): LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

@login_required
def workout_index(request):
  workouts = Workout.objects.filter(user=request.user)
  return render(request, 'workouts/index.html', {'workouts': workouts})

@login_required
def workout_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  set_form = SetForm()
  return render(request, 'workouts/detail.html', {'workout': workout, 'set_form': set_form })

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  form_class = WorkoutForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    return reverse('workout-detail', kwargs={'workout_id': self.object.id})
  
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  fields = ['date', 'title', 'duration', 'description']

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'

@login_required
def add_set(request, workout_id):
  form = SetForm(request.POST)
  if form.is_valid():
    new_set = form.save(commit=False)
    new_set.workout_id = workout_id
    new_set.save()
  return redirect('workout-detail', workout_id=workout_id)

@login_required
def set_delete(request, workout_id, set_id):
  if request.method == 'POST':
    set_to_delete = Set.objects.get(id=set_id)
    set_to_delete.delete()
    return redirect('workout-detail', workout_id=workout_id)
  else:
    return redirect('workout-detail', workout_id=workout_id)

