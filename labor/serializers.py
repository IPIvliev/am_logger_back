from rest_framework import routers, serializers, viewsets
from .models import Report, Checklist, Answer, Question

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'comment']

class ReportSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    # questions = serializers.ReadOnlyField(source='question.title')
    # questions = serializers.RelatedField(source='question', read_only=True)
    class Meta:
        model = Report
        fields = ['id', 'title', 'car_necessary', 'questions', 'comment', 'created_at']


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.title')
    image = serializers.ImageField(required=False)
    class Meta:
        model = Answer
        fields = ['id', 'question', 'comment', 'answer_result', 'image', 'period_at', 'created_at']

class ChecklistSerializer(serializers.ModelSerializer):
    report_title = serializers.ReadOnlyField(source='report_title.title')
    company_name = serializers.ReadOnlyField(source='company_title.name')
    car_number = serializers.ReadOnlyField(source='car_number.number')
    answers = AnswerSerializer(read_only=True, many=True)
    
    class Meta:
        model = Checklist
        fields = ['id', 'report_title', 'company_name', 'car_number', 'answers', 'finish', 'period', 'created_at']

    # def create(self, validated_data):
    #     print("validated_data")
    #     print(validated_data["answers"])
    #     return Answer.objects.create(**validated_data)
