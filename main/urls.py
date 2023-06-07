from django.contrib import admin
from django.urls import path
from .views import(
    HomeView,
    AppView
    
)


urlpatterns = [
    path('', HomeView, name="home"),
    path('app/', AppView, name="app"),
]
