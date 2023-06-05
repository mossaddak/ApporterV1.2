from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import(
    campaign
)

# Create your views here.
@login_required(login_url='login')  
def HomeView(request):


    context = {
        
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')  
def AppView(request):

    campaigns = campaign.objects.all() 

    context = {
        "campaigns":campaigns
    }
    return render(request, 'app.html', context)
