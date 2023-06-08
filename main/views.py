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
    campaign_review,
    appkeyword_screenshot
)
from user_profile.models import(
    User
)

from datetime import datetime, timedelta
from django.db.models import Count

# Create your views here.
@login_required(login_url='login')  
def HomeView(request):

    all_data = app_screenshot.objects.all()
    average_rating = all_data.aggregate(Avg('ratings'))
    average_rating_percentage = (average_rating['ratings__avg'] / 5) * 100  # Assuming ratings are on a scale of 1 to 5

    today = datetime.now().date()
    five_days_ago = today - timedelta(days=4)  # Subtract 4 days to get the range of the last 5 days

    # Retrieve the data for the last five days and calculate the total count for each day
    campaign_review_last_five = campaign_review.objects.filter(created_at__date__range=(five_days_ago, today)) \
        .values('created_at__date') \
        .annotate(total_count=Count('created_at__date'))

    # Format the results as a dictionary mapping date to total count
    campaign_review_last_fiveresult = {entry['created_at__date']: entry['total_count'] for entry in campaign_review_last_five}


    print("Last5===============================", campaign_review_last_fiveresult)
    context = {
        "app":app.objects.all(),
        'average_rating': average_rating['ratings__avg'],
        'total':all_data.count(),
        "AllUser" : User.objects.all().count(),
        "average_rating_percentage":average_rating_percentage,
        "last_five_days_data": campaign_review_last_fiveresult,
    }
    return render(request, 'home.html', context) 


@login_required(login_url='login')  
def AppView(request):

    campaigns = campaign.objects.all() 

    context = {
        "campaigns":campaigns
    }
    return render(request, 'app.html', context)
