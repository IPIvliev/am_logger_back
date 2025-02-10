from django.core.management import BaseCommand
import requests
from main.models import Product
from manufacture.models import Production
import datetime
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

class Command(BaseCommand):
    help = 'Get products. Write --date in format 20241130 for get batchs for the date'

    def add_arguments(self, parser):
        parser.add_argument('--address', type=str)

    def handle(self, *args, **kwargs):
        address = kwargs['address']

        if address:
            message = EmailMessage('Отчёт по работе завода', 'Отчёт во вложении', settings.EMAIL_HOST_USER, [address])
        else:
            message = EmailMessage('Отчёт по работе завода', 'Отчёт во вложении', settings.EMAIL_HOST_USER, ['belov.kk@mag-rf.ru'])
        # message.attach_file("E:/sites/am_logger_back/public_html/media/mail_reports/report_2024.xlsx")
        message.attach_file("/home/razrus/am_logger_back/public_html/media/mail_reports/report_2024.xlsx")
        message.send()

        # send_mail('Отчёт по работе завода', 'Отчёт во вложении', settings.EMAIL_HOST_USER, [address])