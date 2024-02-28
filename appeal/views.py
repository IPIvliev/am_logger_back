from django.shortcuts import render
from rest_framework import generics
from .serializers import AppealSerializer
from .models import Appeal

class AppealList(generics.ListCreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

