import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.db import models
from main.models import Car, Company
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.utils import timezone

DATE_INPUT_FORMATS = ['%d-%m-%Y']

class Report(models.Model):
    title = models.CharField('Наименование отчёта', max_length=255)
    comment = models.TextField('Примечание', null=True, blank=True)
    # questions = models.ManyToManyField(Question)
    car_necessary = models.BooleanField('Добавить автомобиль', null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Отчёт'
        verbose_name_plural='Отчёты'

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.TextField('Соответствие', null=False, blank=False)
    comment = models.TextField('Примечание', null=True, blank=True)
    report = models.ForeignKey(Report, null=True, blank=True, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

    def __str__(self):
        return self.title

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    # checklist = models.ForeignKey(Checklist, on_delete = models.CASCADE, null=True, blank=True)
    answer_result = models.CharField('Результат', null=False, blank=False, default="Нет", max_length=50)
    comment = models.TextField('Комментарий', null=True, blank=True)
    image = models.ImageField('Фотография', upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    period_at = models.IntegerField('Год', validators=[MinValueValidator(2020), max_value_current_year], default=current_year)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'

    def __str__(self):
        return (self.question.title[:50])

def year_choices():
    return [(r,r) for r in range(2020, datetime.date.today().year+1)]

class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

def delete_checklist(Checklist):
    @receiver(pre_delete, sender=Checklist)
    def dc(sender, instance, **kwargs):
        for answer in instance.answers.all(): #for all users who are linked to the DB you're about to kill
            try:
                answer.image.delete()
            except:
                pass
            answer.delete()

class Checklist(models.Model):
    report_title = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='checklists')
    # question_title = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
    company_title = models.ForeignKey(Company, on_delete=models.CASCADE)
    car_number = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)
    finish = models.BooleanField('Сдан', null=False, blank=False, default=False)
    period = models.DateField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Чеклист'
        verbose_name_plural='Чеклисты'
        ordering = ['-created_at']

delete_checklist(Checklist)

class Statistic(models.Model):
    report_title = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='statistics')
    company_title = models.ForeignKey(Company, on_delete=models.CASCADE)
    yes_answers_count = models.IntegerField('Ответы ДА', null=True, blank=True, default=0)
    no_answers_count = models.IntegerField('Ответы НЕТ', null=True, blank=True, default=0)
    empty_answers_count = models.IntegerField('Ответы ПУСТО', null=True, blank=True, default=0)
    period = models.DateField(default=timezone.now())

    class Meta:
        verbose_name='Статистический отчёт'
        verbose_name_plural='Статистические отчёты'

    def __str__(self):
        return (self.report_title.title)