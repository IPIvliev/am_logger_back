import csv
from django.core.management import BaseCommand
from labor.models import Question, Report, Checklist, Answer
from main.models import Company, Car

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        report = Report.objects.get(id=5)
        company = Company.objects.get(name="Самара")

        i = 0

        while i < 6:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                finish = True,
                period = '2022-08-08'
            )

            question = Question.objects.get(id=249)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2022
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1