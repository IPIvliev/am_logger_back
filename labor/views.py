from django.shortcuts import render
from .models import Report, Checklist
from .serializers import ReportSerializer, ChecklistSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ChecklistList(generics.ListAPIView):

    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Checklist.objects.filter(report_title=pk)