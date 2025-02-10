import requests
from main.models import Product
from manufacture.models import Production
from django_mailbox.models import Mailbox
import datetime

def cron_get_products():
    date = str(datetime.date.today()).replace('-', '')
    two_days_ago = str(datetime.date.today() - datetime.timedelta(days=2)).replace('-', '')

    batchs = requests.get('http://virt43/svod-pol/hs/NewProgram/GeProductiontList/'+two_days_ago+'/'+date,
                            headers = {'Authorization': 'Basic SVVTUjo='}).json()
    for item in batchs:
        product_name = item['Production']
        batch_weight = item['Weight']
        batch_number = (item['NumberProductionBatch']).replace(' ', '')
        bacth_creation_date = item['DateOfManufacture']

        product = Product.objects.get_or_create(name=product_name)

        Production.objects.get_or_create(batch=batch_number, product = product[0], weight = batch_weight, created_at = bacth_creation_date)


        # print(date, product_name, batch_weight, batch_number, bacth_creation_date, product[0])

# def get_emails():
#     mailboxes = Mailbox.active_mailboxes.all()

#     for mailbox in mailboxes:
#         messages = mailbox.get_new_mail()