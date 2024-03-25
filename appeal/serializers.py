from rest_framework import serializers
from .models import Appeal, BotUser

class AppealSerializer(serializers.ModelSerializer):
    damage = serializers.ReadOnlyField

    class Meta:
        model = Appeal
        fields = ['id', 'image', 'status', 'phone', 'kp_number', 'comment', 'created_at']

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ['id', 'name', 'uid', 'bot_name']