from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.db.models.functions import TruncDate
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.db.models import Avg
from .models import(
    campaign,
    app,
    app_screenshot,
    campaign_review
)
from user_profile.models import(
    User
)

# Create your views here.
@login_required(login_url='login')  
def HomeView(request):

    all_data = app_screenshot.objects.all()
    average_rating = all_data.aggregate(Avg('ratings'))
    average_rating_percentage = (average_rating['ratings__avg'] / 5) * 100  # Assuming ratings are on a scale of 1 to 5


    today = timezone.now().date()
    five_days_ago = today - timedelta(days=5)
        
    last_five_days_data = campaign_review.objects.filter(created_at__gte=five_days_ago + timedelta(days=1)).annotate(day=TruncDate('created_at')).values('day').annotate(total_reviews=Count('id'))
        



    context = {
        "app":app.objects.all(),
        'average_rating': average_rating['ratings__avg'],
        'total':all_data.count(),
        "AllUser" : User.objects.all().count(),
        "average_rating_percentage":average_rating_percentage,
        "last_five_days_data": last_five_days_data
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')  
def AppView(request):

    campaigns = campaign.objects.all() 

    context = {
        "campaigns":campaigns
    }
    return render(request, 'app.html', context)
