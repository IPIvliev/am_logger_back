from rest_framework import routers, serializers, viewsets
from .models import Report, Checklist, Answer, Question, Statistic
from django.db.models import Q

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

class ShortChecklistSerializer(serializers.ModelSerializer):
    report_title = serializers.ReadOnlyField(source='report_title.title')
    company_name = serializers.ReadOnlyField(source='company_title.name')
    car_number = serializers.ReadOnlyField(source='car_number.number')
    # answers = AnswerSerializer(read_only=True, many=True)
    
    class Meta:
        model = Checklist
        fields = ['id', 'report_title', 'company_name', 'car_number', 'finish', 'period', 'created_at']

class ChecklistSerializer(serializers.ModelSerializer):
    report_title = serializers.ReadOnlyField(source='report_title.title')
    company_name = serializers.ReadOnlyField(source='company_title.name')
    car_number = serializers.ReadOnlyField(source='car_number.number')
    answers = AnswerSerializer(read_only=True, many=True)
    
    class Meta:
        model = Checklist
        fields = ['id', 'report_title', 'company_name', 'car_number', 'answers', 'finish', 'period', 'created_at']

class ReportSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source='group.name')
    questions = QuestionSerializer(read_only=True, many=True)
    finish_checklists = serializers.SerializerMethodField('count_checklists')
    
    def count_checklists(self, report):
        amount = Checklist.objects.filter(finish=True).filter(report_title=report)
        return len(amount)
    
    class Meta:
        model = Report
        fields = ['id', 'title', 'car_necessary', 'period_necessary', 'finish_checklists', 'questions', 'comment', 'created_at', 'group']

class CustomListSerializer(serializers.ModelSerializer):
    report_title = serializers.ReadOnlyField(source='report_title.title')
    company_name = serializers.ReadOnlyField(source='company_title.name')
    car_number = serializers.ReadOnlyField(source='car_number.number')
    yes_answers_count = serializers.SerializerMethodField()
    no_answers_count = serializers.SerializerMethodField()
    empty_answers_count = serializers.SerializerMethodField()

    class Meta:
        model = Checklist
        fields = ['report_title', 'company_name', 'car_number', 'finish', 'yes_answers_count', 'no_answers_count', 'empty_answers_count', 'period', 'created_at']

    def get_yes_answers_count(self, obj):
        return obj.answers.filter(Q(answer_result='Да') | Q(answer_result='да')).count()

    def get_no_answers_count(self, obj):
        return obj.answers.filter(Q(answer_result='Нет') | Q(answer_result='нет')).count()
    
    def get_empty_answers_count(self, obj):
        return obj.answers.filter(answer_result='').count()
    
class StatisticListSerializer(serializers.ModelSerializer):
    report_title = serializers.ReadOnlyField(source='report_title.title')
    company_name = serializers.ReadOnlyField(source='company_title.name')

    class Meta:
        model = Statistic
        fields = ['report_title', 'company_name', 'yes_answers_count', 'no_answers_count', 'empty_answers_count', 'period']

class NumberSerializer(serializers.Serializer):
    number = serializers.CharField()

    # class Meta:
    #     model = Statistic
    #     fields = ['report_title', 'company_name', 'yes_answers_count', 'no_answers_count', 'empty_answers_count', 'period']