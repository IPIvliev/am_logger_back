from django.core.management import BaseCommand
from manufacture.models import Parameter, Equipment
from datetime import datetime, timedelta
from django.db.models import Q
from django.db.models import Count
from statistics import mean
from django.db.models.functions import ExtractHour, TruncDay

class Command(BaseCommand):
    help = 'Archive parameters in equipment for Manufacture'

    # def add_arguments(self, parser):
    #     parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        # path = kwargs['path']
        parameters = Parameter.objects.all()

        for param in parameters:
            if int(param.value) < 0:
                print('ID: '+ str(param.id) + ' Создано: ' + str(param.created_at) + 'Значение было: ' + str(param.value))
                param.value = 0
                param.save()

            elif int(param.value) > 100:
                print('ID: '+ str(param.id) + ' Создано: ' + str(param.created_at) + 'Значение было: ' + str(param.value))
                param.value = 100
                param.save()