from django.core.management import BaseCommand
import requests
from main.models import Product
from manufacture.models import Production
import datetime


class Command(BaseCommand):
    help = 'Get products. Write --date in format 20241130 for get batchs for the date'

    def add_arguments(self, parser):
        parser.add_argument('--date', type=str)

    def handle(self, *args, **kwargs):
        date = kwargs['date']

        if date == None:
            date = str(datetime.date.today()).replace('-', '')

        print(date)

        batchs = requests.get('http://virt43/svod-pol/hs/NewProgram/GeProductiontList/'+date+'/'+date,
                                headers = {'Authorization': 'Basic SVVTUjo='}).json()
        for item in batchs:
            product_name = item['Production']
            batch_weight = item['Weight']
            batch_number = (item['NumberProductionBatch']).replace(' ', '')
            bacth_creation_date = item['DateOfManufacture']

            product = Product.objects.get_or_create(name=product_name)

            Production.objects.get_or_create(batch=batch_number, product = product[0], weight = batch_weight, created_at = bacth_creation_date)


            # print(date, product_name, batch_weight, batch_number, bacth_creation_date, product[0])