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
        time_now = datetime.now()
        day_ago = time_now - timedelta(1)
        month_ago = time_now - timedelta(30)

        params_day_month = Parameter.objects.filter(Q(created_at__lte=day_ago), Q(created_at__gte=month_ago))
        params_month_ago = Parameter.objects.filter(Q(created_at__lte=month_ago))
        
            
        days_in_params_day_month = params_day_month.annotate(day=TruncDay('created_at')).values_list('day')
        days_in_params_day_month = list(set(days_in_params_day_month))

        equipments = Equipment.objects.all()

        for equipment in equipments:

            names_for_params = params_day_month.filter(equipment = equipment.id)

            names_for_params = list(set(names_for_params.values_list('name', flat = True)))

            for name_for_params in names_for_params:

                for item_day in days_in_params_day_month:

                    print("Дата дня: ", item_day[0])    

                    sample_day = params_day_month.filter(created_at__day = item_day[0].day, created_at__month = item_day[0].month, equipment = equipment.id)

                    print("Кол-во записей в день: ", sample_day.count())

                    hours_in_sample_day = sample_day.annotate(hour=ExtractHour('created_at')).values_list('hour', flat = True)

                    hours_in_sample_day = list(set(hours_in_sample_day))

                    for item_hour in hours_in_sample_day:
                        print(item_day[0] + timedelta(hours=item_hour, minutes = 30), item_hour)  

                        sample_hour = sample_day.filter(created_at__hour = item_hour)
                        params_day_month_hour_average_array = []

                        for sample_hour_item in sample_hour:
                            params_day_month_hour_average_array.append(int(sample_hour_item.value))

                        Parameter.objects.create(name = name_for_params, equipment_id = equipment.id, value = int(mean(params_day_month_hour_average_array)), created_at = item_day[0] + timedelta(hours=item_hour, minutes = 30))

                        print(item_hour, sample_hour.count(), int(mean(params_day_month_hour_average_array)))

                   