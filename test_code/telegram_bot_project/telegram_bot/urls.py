# telegram_bot_app/urls.py
from django.urls import path, include
from .views import UserCreateView, MessageCreateView, MessageListView, LoginView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('send-message/', MessageCreateView.as_view(), name='send-message'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('api-auth/', include('rest_framework.urls')),

    
]
