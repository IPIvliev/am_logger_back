from rest_framework import serializers
from .models import Appeal

class AppealSerializer(serializers.ModelSerializer):
    damage = serializers.ReadOnlyField

    class Meta:
        model = Appeal
        fields = ['id', 'image', 'kp_number', 'comment']