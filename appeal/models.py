from django.db import models
from django.utils.html import mark_safe

STATUS_CHOICES = (
    ('N', 'Новое'),
    ('W', 'В работе'),
    ('C', 'Закрыто'),
)

class Appeal(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N')
    comment = models.TextField('Комментарий', null=True, blank=True)
    kp_number = models.CharField('Номер контейнерной площадки', max_length=35, null=False, blank=False)
    image = models.ImageField('Фотография', upload_to='appeals/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Обращение гражданина'
        verbose_name_plural='Обращения граждан'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" />' % (self.image))

    image_tag.short_description = 'Обзорное фото'

    def large_image_tag(self):
        return mark_safe('<img src="/media/%s" width="480" />' % (self.image))

    large_image_tag.short_description = 'Обзорное фото'