from rest_framework import routers, serializers, viewsets
from .models import Report, Checklist, Answer, Question

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'comment']




class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.title', read_only=True)
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

class ReportSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    finish_checklists = serializers.SerializerMethodField('count_checklists')
    
    def count_checklists(self, report):
        amount = Checklist.objects.filter(finish=True).filter(report_title=report)
        return len(amount)
    
    class Meta:
        model = Report
        fields = ['id', 'title', 'car_necessary', 'finish_checklists', 'questions', 'comment', 'created_at']