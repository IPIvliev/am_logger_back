from django.db import models
# from datetime import datetime
from django.utils import timezone

class Equipment(models.Model):
    name = models.CharField('Наименование', max_length=155)
    comment = models.TextField('Примечание', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Оборудование'
        verbose_name_plural='Оборудование'

    def __str__(self):
        return self.name
    
class Parameter(models.Model):
    name = models.CharField('Наименование', null=False, blank=False, max_length=155)
    equipment = models.ForeignKey(Equipment , on_delete=models.CASCADE, related_name='params')
    value = models.CharField('Значение', null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Параметр оборудования'
        verbose_name_plural='Параметры оборудования'

    def __str__(self):
        return self.name

class StopReport(models.Model):
    created_at = models.DateTimeField('Начало простоя', default=timezone.now)
    finished_at = models.DateTimeField('Окончание простоя', default=timezone.now)
    status = models.BooleanField('Статус', default = False)

    class Meta:
        verbose_name='Простой'
        verbose_name_plural='Простои'

    def stop_period(self):
        return str((self.finished_at - self.created_at)).split(".")[0]

    def __str__(self):
        return str(self.created_at)