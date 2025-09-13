from rest_framework import generics, permissions
from .models import Greeting
from .serializers import GreetingSerializer

class GreetingListCreate(generics.ListCreateAPIView):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    permission_classes = [permissions.AllowAny]  # sin auth (challenge)

class GreetingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    permission_classes = [permissions.AllowAny]