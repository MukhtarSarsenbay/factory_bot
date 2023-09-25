# Your project's urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('telegram_bot.urls')),  # Include your app's URLs here
]
