from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'project'
urlpatterns = [
    path('project/', views.project_view, name='project'),

]