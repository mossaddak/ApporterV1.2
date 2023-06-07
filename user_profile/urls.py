from django.contrib import admin
from django.urls import path,include
from .views import (
    SingUpView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('login/', LoginView, name="login"),
    path('singup/', SingUpView, name="singup"),
    path('logout/',LogoutView, name="logout" ),
]
