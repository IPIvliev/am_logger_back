from rest_framework import generics
from .serializers import CompanyPolygonSerializer
from .models import CompanyPolygon
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
import requests
import json
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

class CompanyPolygonList(generics.ListCreateAPIView):
    queryset = CompanyPolygon.objects.all()
    serializer_class = CompanyPolygonSerializer

class UserCompanyPolygonCheck(APIView):
    # serializer_class = CompanyPolygonSerializer(companypolygon)

    def get(self, request):
        username = self.request.query_params.get('username')

        user = User.objects.get(username=username)
        print(user)

        try:
            companypolygon = CompanyPolygon.objects.get(user = user)
            object = [{'name': companypolygon.name, 'inn': companypolygon.inn, 'director': companypolygon.director, 'created_at' : companypolygon.created_at}]

            return Response(object)
        except:
            print("Нет компании")
            return Response({"Нет компании"})
        
    def post(self, request):
        user = User.objects.get(username = request.data['params']['username'])
        print(request.data['params']['username'])
        companypolygon_new = CompanyPolygon.objects.get_or_create(
            name=request.data['params']['company_name'],
            inn=request.data['params']['inn'],
            user=user
        )
 
        return Response({'post': 'Компания привязана!'})

        
class CheckINN(APIView):
    def get(self, request):
        inn = self.request.query_params.get('CompanyINN')
        print(inn)
        payload = json.dumps({
            "CompanyINN": inn
        })
        response = requests.post('http://web1/bpMobileTiket/hs/PersonalAccount/contracts',
                        headers = {'Authorization': 'Basic T2JtZW46T2JtZW4='},
                        data = payload)
        
        try:
            return Response(response.json())
        except:
            return Response(response.text)
    
class CreateAccount(APIView):
    def post(self, request):
        password = User.objects.make_random_password()

        if (request.data['Email'] == '' or request.data['Company_Name'] == '' or request.data['Company_INN'] == ''):
            return Response({ "answer": "Произошла ошибка"})
        if (request.data['Email'] == None or request.data['Company_Name'] == None or request.data['Company_INN'] == None):
            return Response({ "answer": "Произошла ошибка"})
        
        try: 
            user = User.objects.create(
                username = request.data['Email'],
                email = request.data['Email'],
                # password = password
            )
            user.set_password(password)
            user.save()

            group = Group.objects.get(name='Полигон') 
            group.user_set.add(user)
        except:
            return Response({"answer": "Пользователь с указанным инн или email уже существует!"})
        
        company, index = CompanyPolygon.objects.get_or_create(
            name=request.data['Company_Name'],
            inn=request.data['Company_INN'],
        )

        company.users.add(user)

        html_content = render_to_string(
            "emails/registered.html",
            context={ 'password': password,
                      'email': request.data['Email'],
                      'company_name': request.data['Company_Name'],
                      'company_inn': request.data['Company_INN'] },
        )
        
        message = EmailMultiAlternatives('Регистрация в сервисе на вывоз отходов на полигон МАГ-1', html_content,
                            #    'Вы были успешно зарегистрированы в сервисе вывоза отходов полигона МАГ-1. Ваш временный пароль: {{password}}. Войти можно по ссылке: https://vmpro.mag-rf.ru', 
                               settings.EMAIL_HOST_USER, [request.data['Email']])
        message.attach_alternative(html_content, "text/html")

        message.send()
        
 
        return Response({'answer': 'Пользователь создан успешно!'})

class ResetPassword(APIView):
    def post(self, request):
        password = User.objects.make_random_password()
        print(request.data['params']['Email'])

        if (request.data['params']['Email'] == ''):
            return Response({ "answer": "Произошла ошибка"})
        if (request.data['params']['Email'] == None):
            return Response({ "answer": "Произошла ошибка"})
        
        try: 
            user = User.objects.get(
                email = request.data['params']['Email'],
            )

            user.set_password(password)
            user.save()

        except:
            return Response({"answer": "Пользователь с указанным email не найден!"})
        

        html_content = render_to_string(
            "emails/reset_password.html",
            context={ 'password': password,
                      'email': request.data['params']['Email']
                    }
        )
        
        message = EmailMultiAlternatives('Восстановление пароля в сервисе на вывоз отходов на полигон МАГ-1', html_content,
                            #    'Вы были успешно зарегистрированы в сервисе вывоза отходов полигона МАГ-1. Ваш временный пароль: {{password}}. Войти можно по ссылке: https://vmpro.mag-rf.ru', 
                               settings.EMAIL_HOST_USER, [request.data['params']['Email']])
        message.attach_alternative(html_content, "text/html")

        message.send()
 
        return Response({'answer': 'Пароль успешно изменён и отправлен на Вашу почту!'})

class CreateOrder(APIView):
    def post(self, request):
        print("request.data['CompanyINN']", request.data['CompanyINN'])
        if (request.data['CompanyINN'] == '' or request.data['OrderDate'] == '' or request.data['OrderCar'] == '' or request.data['OrderDriver'] == ''):
            return Response({ "answer": "Произошла ошибка"})
        
        payload = json.dumps({
            "CompanyINN": request.data['CompanyINN'],
            "OrderDate": request.data['OrderDate'],
            "OrderCar": request.data['OrderCar'],
            "OrderDriver": request.data['OrderDriver']
        })
        response = requests.post('http://virt43/svod-pol/hs/PersonalAccount/create_order',
                        headers = {'Authorization': 'Basic SVVTUjo='},
                        data = payload)
        print(response.text)
        try:
            return Response(response.json())
        except:
            return Response(response.text)
    
class CheckOrder(APIView):
    def get(self, request):

        payload = json.dumps({
            "OrderID": self.request.query_params.get('OrderID')
        })

        response = requests.post('http://virt43/svod-pol/hs/PersonalAccount/get_status',
                        headers = {'Authorization': 'Basic SVVTUjo=',
                                   'Content-Type': 'application/json'},
                        data = payload)
        
        try: 
            return Response(response.json())
        except:
            return Response(response.text)
    
class CheckOrders(APIView):
    def get(self, request):

        payload = json.dumps({
            "CompanyINN": self.request.query_params.get('CompanyINN'),
            "StartDate": self.request.query_params.get('StartDate'),
            "EndDate": self.request.query_params.get('EndDate'),
        })
        response = requests.post('http://virt43/svod-pol/hs/PersonalAccount/orders',
                        headers = {'Authorization': 'Basic SVVTUjo='},
                        data = payload)
        
        try: 
            return Response(response.json())
        except:
            return Response({'answer': response.text})
        
class GetEvents(APIView):
    def get(self, request):

        payload = json.dumps({
            "CompanyINN": self.request.query_params.get('CompanyINN'),
        })
        response = requests.post('http://virt43/svod-pol/hs/PersonalAccount/get_events',
                        headers = {'Authorization': 'Basic SVVTUjo='},
                        data = payload)
        
        try: 
            return Response(response.json())
        except:
            return Response({'answer': response.text})