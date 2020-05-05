""" Urls """
from django.urls import path
from . import views

app_name = 'charts'
urlpatterns = [
    path('', views.chart01, name='chart01'),
    path('chartmax/<int:pk_value>', views.chartmax, name='chartmax'),
    path('chartsum/<int:pk_value>', views.chartsum, name='chartsum'),
    path('chartdetail/<int:pk_value>', views.chartdetail, name='chartdetail'),
    #path('post/', views.workoutadd, name='post'),
    #path('<int:pk>/', views.WorkoutDetailView.as_view(), name='detail'),
    #path('edit/<int:pk>/', views.edit, name='edit'),
    #path('delete/<int:pk>/', views.delete, name='delete'),
]
