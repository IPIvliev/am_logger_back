from rest_framework import serializers
from .models import Equipment, Parameter, StopReport

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'created_at']

class ParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = ['id', 'equipment', 'name', 'value', 'created_at']

class StopReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = StopReport
        fields = ['id', 'created_at', 'finished_at', 'stop_period', 'status']