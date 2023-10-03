from django.shortcuts import render
from .models import Report, Checklist, Answer, Question
from .serializers import ReportSerializer, ChecklistSerializer, AnswerSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class AnswerUpdate(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ChecklistDestroy(generics.DestroyAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistUpdate(generics.UpdateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistList(generics.ListCreateAPIView):

    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Checklist.objects.filter(report_title=pk)
    
    def perform_create(self, serializer):
        # answers.clear()
        # print("peform_create")
        # print(self)
        answers = []
        company_title_id = self.request.data.get('company_title_id')
        report_title_id = self.request.data.get('report_title_id')
        car_number_id = self.request.data.get('car_number_id')
        try: 
            for answer in self.request.data.get('answers'):
                print(answer)
                print(answer)
                question = Question.objects.get(title = answer['question'])
                new_answer = Answer.objects.create(question = question, comment = answer['comment'], answer_result = answer['answer_result'], image = answer['image'])
                answers.append(new_answer)
        except:
            print("Error!!")
       

        serializer.save(company_title_id = company_title_id, report_title_id = report_title_id, car_number_id = car_number_id, answers = answers)
        answers.clear()
