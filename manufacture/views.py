from rest_framework import generics
from .serializers import EquipmentSerializer, ParameterSerializer, StopReportSerializer, ProductionSerializer
from .models import Equipment, Parameter, StopReport, Production
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
import logging
from itertools import chain
from datetime import datetime, timedelta
from django.utils import timezone, dateformat

logger = logging.getLogger(__name__)

class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ParameterList(generics.ListAPIView):
    serializer_class = ParameterSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = Parameter.objects.filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date), equipment = pk).order_by("-created_at")

        return queryset

class AllParameterList(generics.ListAPIView):
    serializer_class = ParameterSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = Parameter.objects.filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date)).order_by("-created_at")

        return queryset
    
class LastParameterList(generics.ListAPIView):
    serializer_class = ParameterSerializer

    def get_queryset(self):
        now = timezone.localtime(timezone.now())
        minute_ago = now - timedelta(hours=0, minutes=1)

        PowerBAG1 = Parameter.objects.filter(Q(created_at__gte=minute_ago) & Q(created_at__lte=now) & Q(name = 'PowerBAG1'))
        PowerBAG1 = check_last_parameter(PowerBAG1)

        PowerBAG2 = Parameter.objects.filter(Q(created_at__gte=minute_ago) & Q(created_at__lte=now) & Q(name = 'PowerBAG2'))
        PowerBAG2 = check_last_parameter(PowerBAG2)

        SensorBAG1 = Parameter.objects.filter(Q(created_at__gte=minute_ago) & Q(created_at__lte=now) & Q(name = 'SensorBAG1'))
        SensorBAG1 = check_last_parameter(SensorBAG1)

        SensorBAG2 = Parameter.objects.filter(Q(created_at__gte=minute_ago) & Q(created_at__lte=now) & Q(name = 'SensorBAG2'))
        SensorBAG2 = check_last_parameter(SensorBAG2)

        queryset = chain(PowerBAG1, PowerBAG2, SensorBAG1, SensorBAG2)

        return queryset

def check_last_parameter(object):
    if ((object.count() > 1) | (object.count() < 1)):
        equipment = Equipment.objects.get(id = 1)
        object = [{'name': 'PowerBAG1', 'equipment': equipment, 'value' : 0, 'id' : 1, 'created_at' : timezone.localtime(timezone.now())}]
        return object
    else:
        return object

def check_if_stop(value):
    timenow = timezone.localtime(timezone.now())

    last_stop_report = StopReport.objects.last()

    PowerBagNull = Parameter.objects.filter(Q(created_at__year=timenow.year) & Q(created_at__month=timenow.month) & Q(created_at__day=timenow.day) & Q(created_at__hour=timenow.hour) & Q(created_at__minute=timenow.minute) & Q(value = 0) & (Q(name = 'PowerBAG1') | Q(name = 'PowerBAG2')))
    
    if (last_stop_report.status == True) & (value == 0):
        if PowerBagNull.count() > 0:
            StopReport.objects.create()
    elif (last_stop_report.status == False) & (value == 0):
        last_stop_report.finished_at = datetime.now()
        last_stop_report.save()
    elif (last_stop_report.status == False) & (value != 0):
        last_stop_report.finished_at = datetime.now()
        last_stop_report.status = True
        last_stop_report.save()

        if (last_stop_report.finished_at.replace(tzinfo=None) - last_stop_report.created_at.replace(tzinfo=None)).seconds-10800 < 300:
            last_stop_report.delete()
    else:
        pass

class ParameterAdd(generics.CreateAPIView):

    serializer_class = ParameterSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        equipment = generics.get_object_or_404(Equipment, id=pk)

        serializer.validated_data['value'] = int(serializer.validated_data['value'].split(';')[0])

        if serializer.validated_data['value'] < 0:
            serializer.validated_data['value'] = 0

        if serializer.validated_data['value'] > 100:
            serializer.validated_data['value'] = 100

        # if (serializer.validated_data['value'] == 0) & ("Power" in serializer.validated_data['name']):
        if "Power" in serializer.validated_data['name']:
            check_if_stop(serializer.validated_data['value'])
        # elif ((serializer.validated_data['value'] != 0) & ("Power" in serializer.validated_data['name'])):
        #     check_if_stop(serializer.validated_data['value'])

        # last_parameter_value = Parameter.objects.last()

        return serializer.save(equipment=equipment)
    
class StopReportList(generics.ListAPIView):
    queryset = StopReport.objects.all().order_by("-created_at")
    serializer_class = StopReportSerializer

class ProductionList(generics.ListAPIView):
    serializer_class = ProductionSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = Production.objects.filter(Q(created_at__gte=start_date), Q(created_at__lte=end_date)).order_by("-created_at")

        return queryset