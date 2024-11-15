from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'about'
urlpatterns = [
    path('about/', views.about_view, name='about'),

]
