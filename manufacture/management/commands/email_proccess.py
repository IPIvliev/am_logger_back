from django.core.management import BaseCommand
from django_mailbox.models import Mailbox, Message, MessageAttachment
import datetime

from manufacture.services.add_sensor import add_sensor
from manufacture.services.add_power import add_power
from manufacture.services.add_personal import add_personal
from manufacture.services.report_production import report_production
from manufacture.services.report_production_digital import report_production_digital
from manufacture.services.report_work import report_work

class Command(BaseCommand):
    help = 'Write a report'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        mailbox = Mailbox.objects.get(name='info-vmpro@mag-rf.ru')

        print(mailbox)

        add_sensor()
        add_power()
        report_production_digital()

        messages = Message.objects.all()

        for message in messages:
            if message.read == None:
                message.read = datetime.datetime.now()

                attachments = MessageAttachment.objects.filter(message=message)

                for attachment in attachments:
                    # if "производства" in attachment.get_filename().lower():
                    #     report_production(attachment)
                    #     message.save()
                    if "диаграмма" in attachment.get_filename().lower():
                        report_work(attachment, 1440)
                        # message.save()
                    elif "персонал" in attachment.get_filename().lower():
                        add_personal(attachment)
                        # message.save()