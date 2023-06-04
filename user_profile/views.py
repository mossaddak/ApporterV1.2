from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import (
    UserRegistrations,
    LoginForm,
    
)
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .decorators import(
    not_logged_in_required
)
from django.contrib.auth.decorators import login_required
from .models import(
    User
) 

# Create your views here.
@never_cache
def SingUpView(request):

    form = UserRegistrations()
    if request.method == "POST":
        form = UserRegistrations(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registrations Successfully done!")
            return redirect("/")
        else:
            print(form.errors)
            
    context ={
        "form":form
    } 
    return render(request, 'sing_up.html', context)



@never_cache
@not_logged_in_required
def LoginView(request):

    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data.get('username'),
                password=login_form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect("home")

            else:
                messages.warning(request, "You've given wron information, try again!")
                return redirect("/")

    context = {
        "login_form": login_form
    }
    return render(request, 'login.html', context)


# logout user
@never_cache
def LogoutView(request):
    logout(request)
    return redirect("/")
