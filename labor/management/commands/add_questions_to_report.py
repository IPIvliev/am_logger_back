import csv
from django.core.management import BaseCommand
from labor.models import Question, Report, Checklist, Answer
from main.models import Company

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, delimiter=';')

            for row in reader:
                # print(row[1])
                report = Report.objects.get(id = 6)
                Question.objects.create(
                    title='2022 ' + row[1],
                    comment=row[2],
                    report=report
                )

            
            