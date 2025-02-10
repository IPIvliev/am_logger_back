from datetime import datetime, timedelta
from manufacture.models import Parameter
from manufacture.services.write_to_report import write_to_report
from django.db.models import Avg
from django.db.models.functions import Cast
from django.db.models import IntegerField

def add_power():
    yesterday_date = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday_date.replace(hour=0, minute=0, second=0, microsecond=0)

    digital_data = Parameter.objects.filter(created_at__year = yesterday_date.year,
                                            created_at__month = yesterday_date.month,
                                            created_at__day = yesterday_date.day)
    
    power_1 = digital_data.filter(name='PowerBAG1').annotate(as_int=Cast('value', IntegerField())).aggregate(Avg('as_int'))
    power_2 = digital_data.filter(name='PowerBAG2').annotate(as_int=Cast('value', IntegerField())).aggregate(Avg('as_int'))

    if power_1['as_int__avg'] == None:
        power_1['as_int__avg'] = 0
    
    if power_2['as_int__avg'] == None:
        power_2['as_int__avg'] = 0

    try:
        text_data = 'Пакетовскрыватель 1: ' + str(int(power_1['as_int__avg'])) + '% / 60%' + '\n' + 'Пакетовскрыватель 2: ' + str(int(power_2['as_int__avg'])) + '% / 60%\n'
    except:
        text_data = 'Пакетовскрыватель 1: 0% \n Пакетовскрыватель 2: 0% \n'

    # print(text_data)

    write_to_report(20, yesterday_date, str(int(power_1['as_int__avg'])))
    write_to_report(21, yesterday_date, str(int(power_2['as_int__avg'])))
    write_to_report(22, yesterday_date, '60')