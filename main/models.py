from django.db import models

class Company(models.Model):
    name = models.CharField('Наименование', max_length=155)
    comment = models.TextField('Примечание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Контрагент'
        verbose_name_plural='Контрагенты'

    def __str__(self):
        return self.name

class Car(models.Model):
    number = models.CharField('Номер автомобиля', max_length=28)
    company = models.ForeignKey(Company , on_delete=models.PROTECT, related_name='cars')
    comment = models.TextField('Примечание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Автомобиль'
        verbose_name_plural='Автомобили'

    def __str__(self):
        return self.number