import csv
from django.core.management import BaseCommand
from labor.models import Question, Report, Checklist, Answer
from main.models import Company, Car

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        report = Report.objects.get(id=1)
        company = Company.objects.get(name="Пенза")

        new_answers = []
        print("Start")
        with open(path, 'rt') as f:
            reader = csv.DictReader(f, delimiter=';')
            headers = reader.fieldnames

            all_cars = list(filter(lambda k: 'car_' in k, headers))
            cars = [w.replace('car_', '') for w in all_cars]

            for car in cars:
                new_answers.clear()
                with open(path, 'rt') as f:
                    reader = csv.DictReader(f, delimiter=';')
                    car_number = Car.objects.get(number=car)
                    # print('Машина: ', car, car_number, report, company)
                    checklist = Checklist.objects.create(
                        report_title = report,
                        company_title = company,
                        car_number = car_number,
                        finish = True,
                        period = '2023-06-20'
                    )
                    for row in reader:
                        question = Question.objects.get(title=row['Document'])
                        # print(row['Number'], row['Document'], question, row['car_' + car])
                        
                        new_answer = Answer.objects.create(
                            question = question,
                            answer_result = row['car_' + car],
                        )
                        new_answers.append(new_answer)

                    checklist.answers.set(new_answers)
                    checklist.save()

                    print(new_answers)