import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.db import models
from main.models import Car, Company

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
    answer = models.BooleanField('Результат', null=False, blank=False, default=False)
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

class Checklist(models.Model):
    report_title = models.ForeignKey(Report, on_delete=models.CASCADE)
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





