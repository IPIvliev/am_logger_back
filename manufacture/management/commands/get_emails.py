from django.core.management import BaseCommand
from django_mailbox.models import Mailbox

class Command(BaseCommand):
    help = 'Get emails for info-vmpro@mag-rf.ru'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        mailboxes = Mailbox.active_mailboxes.all()

        for mailbox in mailboxes:
            print(mailbox.name)
            messages = mailbox.get_new_mail()
            for message in messages:
                print(
                    'Received %s (from %s)',
                    message.subject,
                    message.from_address
                )