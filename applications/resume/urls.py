from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'resume'
urlpatterns = [
    path('resume/',views.resume_view, name='resume'),
    path('test/',views.TestView.as_view(), name='test'),

]