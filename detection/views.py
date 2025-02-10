from django.shortcuts import render
from rest_framework import generics
from detection.serializers import RecognitionSerializer
from detection.models import Recognition
from django.db.models import Q

class RecognitionList(generics.ListAPIView):
    serializer_class = RecognitionSerializer

    def get_queryset(self):
        car_number = self.request.query_params.get('car_number')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if (car_number == None):
            queryset = Recognition.objects.filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date))
        else:
            queryset = Recognition.objects.filter(plate_text=car_number).filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date))

        return queryset
