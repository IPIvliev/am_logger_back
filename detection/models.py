from django.db import models
from detection.singleton_model import SingletonModel
from django.utils.html import format_html

class Camera(models.Model):
    name = models.CharField('Наименование', max_length=155)
    url = models.CharField('URL', max_length=155)
    comment = models.TextField('Примечание', null=True, blank=True)
    status = models.BooleanField('Статус', default = False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Камера'
        verbose_name_plural='Камеры'

    def __str__(self):
        return self.name
    
class Recognition(models.Model):
    plate_text = models.CharField('Номер автомобиля', max_length=155, null=False, blank=False)
    source = models.ForeignKey(Camera, on_delete=models.PROTECT, related_name='recognitions')
    plate_image = models.ImageField('Фотография номера', upload_to='plates/')
    car_image =  models.ImageField('Фотография с камеры', upload_to='cars/')
    ratio = models.FloatField('Коэфициент распознавания', default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Распознавание'
        verbose_name_plural='Распознавания'

    def __str__(self):
        return self.plate_text

class DetectionSettings(SingletonModel):
    confidence_threshold = models.FloatField('Чувствительность определения', default=0)
    delay = models.IntegerField('Задержка для записи в БД (секунды)', default=0)
    plate_file = models.FileField('Файл модели номера', upload_to = 'models/', null=True, blank=True)
    symbol_file = models.FileField('Файл модели знаков', upload_to = 'models/', null=True, blank=True)

    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.plate_file.url))

    def __str__(self):
        return 'Настройка определения номеров'
