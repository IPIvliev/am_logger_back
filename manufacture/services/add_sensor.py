from datetime import datetime, timedelta
from manufacture.models import Parameter
from manufacture.services.write_to_report import write_to_report
from django.db.models import Avg
from django.db.models.functions import Cast
from django.db.models import IntegerField

def add_sensor():
    yesterday_date = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday_date.replace(hour=0, minute=0, second=0, microsecond=0)

    digital_data = Parameter.objects.filter(created_at__year = yesterday_date.year,
                                            created_at__month = yesterday_date.month,
                                            created_at__day = yesterday_date.day)
    
    sensor_1 = digital_data.filter(name='SensorBAG1').annotate(as_int=Cast('value', IntegerField())).aggregate(Avg('as_int'))
    sensor_2 = digital_data.filter(name='SensorBAG2').annotate(as_int=Cast('value', IntegerField())).aggregate(Avg('as_int'))

    if sensor_1['as_int__avg'] == None:
        sensor_1['as_int__avg'] = 0
    
    if sensor_2['as_int__avg'] == None:
        sensor_2['as_int__avg'] = 0

    try:
        text_data = 'Пакетовскрыватель 1: ' + str(int(sensor_1['as_int__avg'])) + '% / 90%' + '\n' + 'Пакетовскрыватель 2: ' + str(int(sensor_2['as_int__avg'])) + '% / 90%\n'
    except:
        text_data = 'Пакетовскрыватель 1: 0% \n Пакетовскрыватель 2: 0% \n'


    write_to_report(17, yesterday_date, str(int(sensor_1['as_int__avg'])))
    write_to_report(18, yesterday_date, str(int(sensor_2['as_int__avg'])))
    write_to_report(19, yesterday_date, '90')