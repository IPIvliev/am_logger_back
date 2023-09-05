from django.contrib import admin
from .models import Report, Question, Answer, Checklist

admin.site.site_title = 'Администрирование'
admin.site.site_header = 'Панель управления сервисом "Охрана Труда"'
admin.site.index_title = 'AM LOGGER'


# class ReportInline(admin.TabularInline):
#     model = Report.questions.through
#     extra = 0

admin.site.register(Report)
# admin.site.register(Question)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    # Here
    @admin.display(description='Отчёт')
    def get_reports(self, obj):
        return [report.title for report in obj.report_set.all()]
    
    list_filter = ('report',)
    # list_display = ('title', 'get_reports')
    list_display = ('title', 'report')
    # inlines = [ReportInline]

admin.site.register(Answer)

# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer', 'created_at')

# class AnswerInLine(admin.TabularInline):
#     model = Answer
#     extra = 3

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'created_at', 'car_title', 'company_title')
    # inlines = [AnswerInLine]