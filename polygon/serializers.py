from rest_framework import routers, serializers, viewsets
from .models import CompanyPolygon

class CompanyPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPolygon
        fields = ['id', 'name', 'inn', 'director', 'comment', 'created_at']