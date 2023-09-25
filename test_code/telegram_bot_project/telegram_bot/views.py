# telegram_bot_app/views.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import UserSerializer, MessageSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token  # Import Token model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from rest_framework.authtoken.models import Token

def is_token_valid(user):
    try:
        token = Token.objects.get(user=user)
        return token.created + timezone.timedelta(days=1) > timezone.now()
    except Token.DoesNotExist:
        return False



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            print("user logged in")
            token, created = Token.objects.get_or_create(user=user)
            if is_token_valid:
                return Response({"token": token.key}, status=status.HTTP_200_OK)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    #authentication_classes = (TokenAuthentication,)
   #permission_classes = (IsAuthenticated,)
    

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)
