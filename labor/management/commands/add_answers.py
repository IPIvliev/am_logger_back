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
        new_answers = []
        with open(path, 'rt') as f:
            reader = csv.reader(f, delimiter=';')
            checklist = Checklist.objects.get(id = 75)
            # report = Report.objects.get(id = 6)

            for row in reader:
                # print(row[1])
                title='2022 ' + row[1]
                question = Question.objects.get(title=title)
                
                # print('Answer: ' + question.title + 'row[3]: ' + row[3])
                new_answer = Answer.objects.create(
                    question = question,
                    answer_result = row[9],
                    period_at = 2022
                )
                new_answers.append(new_answer)

            checklist.answers.set(new_answers)
            checklist.save()

            
            