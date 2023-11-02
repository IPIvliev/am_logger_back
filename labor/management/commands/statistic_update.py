from django.core.management import BaseCommand
from labor.models import Question, Report, Checklist, Answer, Statistic
from main.models import Company
from django.db.models import Q

class Command(BaseCommand):
    help = 'Update statictic data'

    def add_arguments(self, parser):
        parser.add_argument('--report_id', type=int)

    def handle(self, *args, **kwargs):
        report_id = kwargs['report_id']

        report = Report.objects.get(id = report_id)

        companies = Company.objects.all()

        for company in companies:
            checklists = Checklist.objects.filter(report_title = report).filter(company_title = company).filter(finish = True)

            statistic_report, created = Statistic.objects.get_or_create(
                report_title = report,
                company_title = company
            )

            yes_amount = 0
            no_amount = 0
            empty_emount = 0

            for checklist in checklists:
                yes_amount += checklist.answers.filter(Q(answer_result='Да') | Q(answer_result='да')).count()
                no_amount += checklist.answers.filter(Q(answer_result='Нет') | Q(answer_result='нет')).count()
                empty_emount += checklist.answers.filter(answer_result='').count()
            
            print(company, no_amount)
            
            statistic_report.yes_answers_count = yes_amount
            statistic_report.no_answers_count = no_amount
            statistic_report.empty_answers_count = empty_emount

            statistic_report.save()          