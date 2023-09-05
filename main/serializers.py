from rest_framework import routers, serializers, viewsets
from .models import Car, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'comment', 'created_at']

class CarSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Car
        fields = ['id', 'number', 'company', 'comment', 'created_at']