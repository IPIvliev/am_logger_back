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

        request_dict = self.request.data.dict()

        answers = []
        company_title_id = self.request.data.get('company_title_id')
        report_title_id = self.request.data.get('report_title_id')
        car_number_id = self.request.data.get('car_number_id')

        image_amount = len([value for key, value in request_dict.items() if '[image]' in key.lower()])
        i = 0

        try: 
            while i < image_amount:
                question = Question.objects.get(title = request_dict['answers['+str(i)+'][question]'])
                new_answer = Answer.objects.create(question = question, comment = request_dict['answers['+str(i)+'][comment]'], 
                                                   answer_result = request_dict['answers['+str(i)+'][answer_result]'], image = request_dict['answers['+str(i)+'][image]'])
                answers.append(new_answer)
                i += 1
        except:
            print("Error!!")
       
        serializer.save(company_title_id = company_title_id, report_title_id = report_title_id, car_number_id = car_number_id, answers = answers)
        answers.clear()

class ChecklistAll(generics.ListCreateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer