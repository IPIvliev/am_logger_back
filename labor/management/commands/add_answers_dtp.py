import csv
from django.core.management import BaseCommand
from labor.models import Question, Report, Checklist, Answer
from main.models import Company, Car

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        report = Report.objects.get(id=3)
        company = Company.objects.get(name="Самара")
        car = Car.objects.get(id = 37)

        dtp_amount = [7,3,4,4,5,3,1,4,0,0,0,0]
        i = 0
        # Январь
        while i < dtp_amount[0]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-01-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Февраль
        while i < dtp_amount[1]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-02-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Март
        while i < dtp_amount[2]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-03-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Апрель
        while i < dtp_amount[3]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-04-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Май
        while i < dtp_amount[4]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-05-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Июнь
        while i < dtp_amount[5]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-06-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Июль
        while i < dtp_amount[6]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-07-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Август
        while i < dtp_amount[7]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-08-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Сентябрь
        while i < dtp_amount[8]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-09-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Октябрь
        while i < dtp_amount[9]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-10-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Ноябрь
        while i < dtp_amount[10]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-11-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

        i = 0
        # Декабрь
        while i < dtp_amount[11]:
            checklist = Checklist.objects.create(
                report_title = report,
                company_title = company,
                car_number = car,
                finish = True,
                period = '2023-12-08'
            )

            question = Question.objects.get(id=247)
            new_answer = Answer.objects.create(
                question = question,
                answer_result = 'Да',
                period_at = 2023
            )
            checklist.answers.set([new_answer])
            checklist.save()
            i += 1

            
            