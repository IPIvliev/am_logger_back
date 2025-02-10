from openpyxl import load_workbook
from datetime import datetime, timedelta
from manufacture.models import Production
from manufacture.services.write_to_report import write_to_report
from itertools import groupby
from operator import itemgetter

def report_production_digital():
    current_month_year = datetime.now().strftime('%m') + '.' + datetime.now().strftime('%Y')
    # current_month_year = '07.2024' # Для тестов

    yesterday_date = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday_date.replace(hour=0, minute=0, second=0, microsecond=0)
    # yesterday_date = '2024-04-16 00:00:00'
    # yesterday_date = datetime.strptime(yesterday_date, "%Y-%m-%d %H:%M:%S")
    
    digital_product_titles = []
    digital_product_values = []

    digital_product_varients = []
    digital_product_weights = []

    text_data = ''

    digital_data = Production.objects.filter(created_at__year = yesterday_date.year,
                                             created_at__month = yesterday_date.month,
                                             created_at__day = yesterday_date.day)


    for item in digital_data:
        if item.product not in digital_product_varients:
            digital_product_varients.append(item.product)

    
    for item in digital_product_varients:
        digital_product_titles.append(item.name)
        item_objects = digital_data.filter(product = item)

        sum_weights = 0

        for itemm in item_objects: 
            sum_weights += int(itemm.weight)


        digital_product_weights.append(sum_weights)

    digital_data = [{'name':a, 'weight':b} for a,b in zip(digital_product_titles, digital_product_weights)]

    for digital_item in digital_data:
        match digital_item['name']:
            case 'ПЭТ микс':
                april_value = 3569
                write_to_report(7, yesterday_date, str(digital_item['weight']))
                write_to_report(8, yesterday_date, str(april_value))
            case 'ПНД':
                april_value = 76
                write_to_report(9, yesterday_date, str(digital_item['weight']))
                write_to_report(10, yesterday_date, str(april_value))
            case 'Алюминий':
                april_value = 304
                write_to_report(11, yesterday_date, str(digital_item['weight']))
                write_to_report(12, yesterday_date, str(april_value))
            case 'Стекло':
                april_value = 1356
                write_to_report(13, yesterday_date, str(digital_item['weight']))
                write_to_report(14, yesterday_date, str(april_value))
            case 'Черный металл':
                april_value = 1355
                write_to_report(15, yesterday_date, str(digital_item['weight']))
                write_to_report(16, yesterday_date, str(april_value))
            case _:
                april_value = 0

    for digital_item in digital_data:
        print(digital_item['name'] + str(digital_item['weight']) + ' / ' + str(april_value) +'\n')

    # print('digital_data: ', digital_data)
    # print('excel_data: ', excel_data)
    # print('text_data: ', text_data)

    # write_to_report(7, yesterday_date, text_data)