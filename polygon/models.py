from django.db import models
from django.contrib.auth.models import User

class CompanyPolygon(models.Model):
    name = models.CharField('Наименование', max_length=155)
    users = models.ManyToManyField(User, related_name='companies_polygon', null=True, blank=True)
    inn = models.CharField('ИНН', max_length=14, null=False, blank=False)
    director = models.CharField('ФИО директора', max_length=155, null=True, blank=True)
    comment = models.TextField('Примечание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Контрагент на полигон'
        verbose_name_plural='Контрагенты на полигон'

    def __str__(self):
        return self.name
