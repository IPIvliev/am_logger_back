from rest_framework import serializers
from detection.models import Recognition

class RecognitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recognition
        fields = ['id', 'plate_text', 'source', 'plate_image', 'car_image', 'ratio', 'created_at']