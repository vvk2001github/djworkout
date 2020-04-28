from django.urls import path
from . import views

app_name='charts'
urlpatterns = [
    path('', views.chart01, name='chart01'),
    path('detail/<int:pk>', views.chart02, name='chart02'),
    #path('post/', views.workoutadd, name='post'),
    #path('<int:pk>/', views.WorkoutDetailView.as_view(), name='detail'),
    #path('edit/<int:pk>/', views.edit, name='edit'),
    #path('delete/<int:pk>/', views.delete, name='delete'),
 ]