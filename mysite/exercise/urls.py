from django.urls import path
from . import views

app_name='exercise'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.postview, name='post'),
    path('<int:pk>/', views.ExerciseDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
 ]