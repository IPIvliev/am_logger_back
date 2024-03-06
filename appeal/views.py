from django.shortcuts import render
from rest_framework import generics
from .serializers import AppealSerializer
from .models import Appeal
from django.db.models import Q

class AppealList(generics.ListCreateAPIView):
    serializer_class = AppealSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = Appeal.objects.filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date))

        return queryset

    # queryset = Appeal.objects.all()
    

