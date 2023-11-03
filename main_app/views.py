from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Set
from django.views.generic.edit import CreateView

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
  # add set form here
  return render(request, 'workouts/detail.html', {'workout': workout })

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = '__all__'

