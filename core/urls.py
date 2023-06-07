from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #user profile
    path('', include('user_profile.urls')),

    #main
    path('', include('main.urls')),

    #google auth
    path("", include("allauth.urls")), 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
