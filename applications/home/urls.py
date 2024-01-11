from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'home'
urlpatterns = [
    path('home/', views.home_view, name='home'),

]