from django.urls import path
from . import views

app_name='workouts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.workoutadd, name='post'),
    path('<int:pk>/', views.WorkoutDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    #path('delete/<int:pk>/', views.delete, name='delete'),
 ]