from django.shortcuts import render
from .models import Report, Checklist, Answer, Question, Statistic
from .serializers import ReportSerializer, ChecklistSerializer, ShortChecklistSerializer, AnswerSerializer, CustomListSerializer, StatisticListSerializer, NumberSerializer
from rest_framework import generics
from django.db.models import Q
# import cv2
from django.http import HttpResponse

class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class AnswerUpdate(generics.UpdateAPIView):
    queryset = Answer.objects.order_by("id")
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

class ChecklistAll(generics.ListAPIView):
    # queryset = Checklist.objects.all().select_related('report_title', 'company_title', 'car_number').prefetch_related('answers').only(
    #     'report_title__title', 'company_title__name', 'car_number__number', 'answers__id', 'answers__question', 'answers__comment',
    #     'answers__answer_result', 'answers__image', 'answers__period_at', 'answers__created_at')
    queryset = Checklist.objects.all()
    # def get_queryset(self, **kwargs):
    #     return Checklist.objects.all()

    serializer_class = ShortChecklistSerializer
    # serializer_class = ChecklistSerializer

class ChecklistCount(generics.ListAPIView):
    queryset = Checklist.objects.all()
    serializer_class = CustomListSerializer


class AnswersList(generics.ListAPIView):
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Answer.objects.filter(checklists__id=pk)
    
    serializer_class = AnswerSerializer

class StatisticCount(generics.ListAPIView):
    # queryset = Statistic.objects.all()
    serializer_class = StatisticListSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        print('Start date: ', start_date)
        queryset = Statistic.objects.filter(Q(period__gte=start_date), Q(period__lte=end_date))
        # queryset = Statistic.objects.all()
        return queryset

    # def get(self, request, format=None):
    #     print("ddd")
    #     checklists = [checklist.report_title for checklist in Checklist.objects.all()]
    #     serializer = CustomListSerializer(checklists, many=True)
    #     print("ddd: ", serializer)
    #     # return checklists
    #     return HttpResponse(json.dumps(serializer), mimetype="application/json")

class GetVideo(generics.ListAPIView):
    serializer_class = NumberSerializer

    def get_queryset(self):
        ip = self.request.query_params.get('camera')
        # vidcap = cv2.VideoCapture('http://' + ip + '/action/stream?subject=mjpeg&user=admin&pwd=admin')

        # success, image = vidcap.read()
        # if success:
        #     # cv2.imwrite("frame%d.jpg" % count, image)
        #     # cv2.imwrite("media/usedVideo/frame%d.jpg" % 1, image)
        #     # cv2.imwrite("frame%d.jpg" % 1, image)
        # # cv2.destroyAllWindows()
        # vidcap.release()

        # queryset = [{'number': 'H 780 HT 152'}]

        # return queryset