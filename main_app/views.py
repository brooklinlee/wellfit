from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return HttpResponse('<h1>About</h1>')
