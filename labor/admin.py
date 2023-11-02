from django.contrib import admin
from .models import Report, Question, Answer, Checklist, Statistic

admin.site.site_title = 'Администрирование'
admin.site.site_header = 'Панель управления сервисом "Охрана Труда"'
admin.site.index_title = 'AM LOGGER'


admin.site.register(Report)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_filter = ('report_title', 'company_title',)
    list_display = ('report_title' ,'company_title', 'yes_answers_count', 'no_answers_count', 'empty_answers_count')

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

# admin.site.register(Answer)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # list_display = ('question', 'answer', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'created_at', 'car_number', 'company_title')
