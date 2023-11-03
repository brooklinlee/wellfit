from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('workouts/', views.workout_index, name='workout-index'),
  path('workouts/<int:workout_id>/', views.workout_detail, name='workout-detail'),
  path('workouts/create', views.WorkoutCreate.as_view(), name='workout-create'),
]